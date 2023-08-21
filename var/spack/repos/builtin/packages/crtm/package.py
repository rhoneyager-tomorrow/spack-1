# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Crtm(CMakePackage):
    """The Community Radiative Transfer Model (CRTM) package.
    The CRTM is composed of four important modules for gaseous transmittance,
    surface emission and reflection, cloud and aerosol absorption and
    scattering, and a solver for a radiative transfer."""

    homepage = "https://www.jcsda.org/jcsda-project-community-radiative-transfer-model"
    git = "https://github.com/JCSDA/crtm.git"
    url = "https://github.com/JCSDA/crtm/archive/refs/tags/v2.3.0.tar.gz"

    maintainers(
        "BenjaminTJohnson",
        "t-brown",
        "edwardhartnett",
        "AlexanderRichert-NOAA",
        "Hang-Lei-NOAA",
        "climbfuji",
    )
    variant(
        "fix", default=False, description='Download CRTM coeffecient or "fix" files (several GBs).'
    )
    variant(
        "build_type",
        default="RelWithDebInfo",
        description="CMake build type",
        values=("Debug", "Release", "RelWithDebInfo", "MinSizeRel"),
    )

    depends_on("cmake@3.15:", type="build")
    depends_on("git-lfs")
    depends_on("netcdf-fortran", when="@2.4.0:")
    depends_on("netcdf-fortran", when="@v2.3-jedi.4")
    depends_on("netcdf-fortran", when="@v2.4-jedi.1")
    depends_on("netcdf-fortran", when="@v2.4-jedi.2")
    depends_on("netcdf-fortran", when="@v2.4.1-jedi")
    depends_on("netcdf-fortran", when="@v3.0.0-rc.1")
    depends_on("netcdf-fortran", when="@v3.0.0-skylabv5")
    depends_on("netcdf-fortran", when="@v3.0.0-skylabv5-1")

    depends_on("crtm-fix@2.3.0_emc", when="@2.3.0 +fix")
    depends_on("crtm-fix@2.4.0_emc", when="@2.4.0 +fix")

    depends_on("ecbuild", type=("build"), when="@v2.3-jedi.4")
    depends_on("ecbuild", type=("build"), when="@v2.4-jedi.1")
    depends_on("ecbuild", type=("build"), when="@v2.4-jedi.2")
    depends_on("ecbuild", type=("build"), when="@v2.4.1-jedi")
    depends_on("ecbuild", type=("build"), when="@v3.0.0-rc.1")
    depends_on("ecbuild", type=("build"), when="@v3.0.0-skylabv5")
    depends_on("ecbuild", type=("build"), when="@v3.0.0-skylabv5-1")

    # Slightly after the Skylab 5 release to fix https://github.com/JCSDA/CRTMv3/pull/48.
    # TODO: Push for a distinct tag in the CRTMv3 repository.
    # Spack gets confused by the different repository url, so we use direct URLs here.
    version("v3.0.0-skylabv5-1", url="https://www.github.com/JCSDA/crtmv3/tarball/d15810f5538d4cf041e94ebfbb41b403d82bed13",
        sha256="fa0f050ae29d3d7d71da4b97c5dfd74ad90c98c3645fd35340efa1410cf76cf3")

    # The official release for Skylab 5, but it's buggy. See https://github.com/JCSDA/CRTMv3/pull/48.
    version("v3.0.0-skylabv5", url="https://www.github.com/JCSDA/crtmv3/tarball/74cdc9428f56a11ce0dcd3ac7ddff00097b7b61c",
        sha256="033abf0dde10b29043f3cde8c4b4285a32e5886599d174ab83ef6f5a2132e3d6")

    version("v2.4.1-jedi.1", sha256="94ff24051382d544c2e200a937bfe7d2047f6393a3e22f64284d5dc70e791ca6")
    version("v2.4.1-jedi", sha256="fd8bf4db4f2a3b420b4186de84483ba2a36660519dffcb1e0ff14bfe8c6f6a14")

    # Both of these have big binary file blobs
    #  Corrects polarization angle biases for NOAA-21 and fixes WMO satellite and sensor ids.
    version("v2.4.0_emc.2", commit="50fde6ae9caeaca3f5c8c3a39aca7e594eab451a")
    #  Adds new NOAA-21 and ancillary files for VIIRS.
    version("v2.4.0_emc.1", commit="eaf322287691d5d204167e1a929117ba6b9c2e23")

    # REL-2.4.0_emc (v2.4.0 ecbuild does not work)
    version("2.4.0", commit="5ddd0d6")
    # Uses the tip of REL-2.3.0_emc branch
    version("2.3.0", commit="99760e6")
    # JEDI applications so far use these versions
    # Branch release/crtm_jedi
    version("v2.3-jedi.4", commit="bfede42")
    # Branch release/crtm_jedi_v2.4.0
    version("v2.4-jedi.1", commit="8222341")
    version("v2.4-jedi.2", commit="62831cb")

    def url_for_version(self, version):
        if self.spec.satisfies("@v3") or version >=  Version("3.0.0"):
            return "https://github.com/JCSDA/crtmv3/archive/refs/tags/{}.tar.gz".format(version)
        else:
            return "https://github.com/JCSDA/crtm/archive/refs/tags/{}.tar.gz".format(version)
