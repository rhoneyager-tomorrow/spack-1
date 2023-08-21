# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Saber(CMakePackage):
    """System-Agnostic Background Error Representation"""

    homepage = "https://github.com/JCSDA/saber"
    git = "https://github.com/JCSDA/saber.git"

    maintainers = ["climbfuji"]

    version('1.7.0', commit='d90ce5276b37552d569fcb72a22b5a30fb03de75')
    version('develop', branch='develop', no_cache=True)

    variant('gsibec', default=True, description='Enable SABER block GSI')
    variant('mkl', default=False, description='Use MKL for LAPACK implementation')
    variant('oops', default=True, description='Use oops')
    variant('openmp', default=True, description='Build with OpenMP support')
    variant('vader', default=True, description='Build with vader support')

    depends_on('ecbuild', type=('build'))
    depends_on('ecbuild@3.3.2:', type=('build'), when='@1.4.0:')
    depends_on('eckit')
    depends_on('eckit@1.23.0', when='@1.7.0')
    depends_on('ecmwf-atlas')
    depends_on('ecmwf-atlas@0.33.0', when='@1.7.0')
    depends_on('ecmwf-atlas+openmp', when='+openmp')
    depends_on('ecmwf-atlas~openmp', when='~openmp')
    depends_on('fckit')
    depends_on('fckit@0.10.1', when='@1.7.0')
    depends_on('gsibec', when='+gsibec')
    depends_on('gsibec@1.1.2', when='@1.7.0 +gsibec')
    depends_on('jedi-cmake', type=('build'))
    depends_on('lapack', when='~mkl')
    depends_on('llvm-openmp', when='+openmp %apple-clang', type=('build', 'run'))
    depends_on('mkl', when='+mkl')
    depends_on('mpi')
    depends_on('netcdf-c')
    depends_on('netcdf-fortran')
    depends_on('oops', when='+oops')
    depends_on('oops+openmp', when='+oops +openmp')
    depends_on('oops~openmp', when='+oops ~openmp')
    depends_on('oops@1.7.0', when='@1.7.0 +oops')
    depends_on('sp', when='+gsibec')
    depends_on('vader', when='+vader')
    depends_on('vader@1.4.0', when='@1.7.0 +vader')

    def cmake_args(self):
        res = [
            self.define_from_variant('ENABLE_MKL', 'mkl'),
            self.define_from_variant('OPENMP',  'openmp')
        ]
        return res

    # Lapack vs MKL bug.
    patch('CMakeLists.txt.patch', when='@1.7.0')
    # Another Lapack vs MKL bug. If ENABLE_MKL was off, then the saber-import.cmake file had a syntax error.
    patch('saber-import.cmake.in.patch', when='@1.7.0')
    # Fixed in develop. JCSDA/saber#22 / JCSDA-internal/saber#652.
    patch('quench.src.Fields.cc.patch', when='@1.7.0')

