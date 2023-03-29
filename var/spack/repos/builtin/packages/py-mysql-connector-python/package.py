# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class PyMysqlConnectorPython(PythonPackage):
    """MySQL Connector/Python is implementing the MySQL Client/Server
    protocol completely in Python. No MySQL libraries are needed, and
    no compilation is necessary to run this Python DB API v2.0
    compliant driver."""

    homepage = "https://github.com/mysql/mysql-connector-python"
    url = "https://github.com/mysql/mysql-connector-python/archive/8.0.13.tar.gz"
    git = "https://github.com/mysql/mysql-connector-python.git"

    version("8.0.32", sha256="42b951f50e11bd1d04f5b596d9e3c48a5a3379403e5b87ca082b621869eade2e")
    version("8.0.13", sha256="d4c0834c583cdb90c0aeae90b1917d58355a4bf9b0266c16fd58874a5607f9d4")

    depends_on("py-setuptools", type="build")

    # Note: protobuf only needed for mysqlx extension, not yet configured
    #depends_on("py-protobuf@3.0.0:3.10.0", type=("build", "run"), when="@8.0.13")
    #depends_on("py-protobuf@3.11.0:3.20.3", type=("build", "run"), when="@8.0.32")

    # Required for the MySQL C extension. Assume that users always want that.
    depends_on("openssl", type=("build"))
    depends_on("mysql", type=("build"))

    # Fixes an issue with files being copied into the build tree multiple times,
    # but these files may not have the write permissions set for the user.
    patch("cpydist.patch", when="@8.0.32")

    def setup_build_environment(self, env):
        env.set("MYSQL_CAPI", os.path.join(self.spec["mysql"].prefix.bin, "mysql_config"))
        env.set("OPENSSL_INCLUDE_DIR", self.spec["openssl"].prefix.include)
        env.set("OPENSSL_LIB_DIR", self.spec["openssl"].prefix.lib)
