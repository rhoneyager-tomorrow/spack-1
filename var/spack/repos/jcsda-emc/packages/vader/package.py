# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Vader(CMakePackage):
    """The VAriable DErivation Repository"""

    homepage = "https://github.com/JCSDA/vader"
    git = "https://github.com/JCSDA/vader.git"

    maintainers = ["climbfuji"]

    version('1.4.0', commit='4264b56111a62ab1339320ad85a7f715b923df47')
    version('develop', branch='develop', no_cache=True)

    depends_on('ecbuild', type=('build'))
    depends_on('ecbuild@3.3.2:', type=('build'), when='@1.4.0:')
    depends_on('jedi-cmake', type=('build'))
    depends_on('mpi')
    depends_on('netcdf-c+mpi')
    depends_on('netcdf-fortran')
    depends_on('oops')
    depends_on('oops@1.7.0', when='@1.4.0')

