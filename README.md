# lrose-netcdf

### NetCDF and HDF5 support for LROSE.

The NetCDF installations managed by OS package managers (e.g. yum, dpkg) can vary,
since the NetCDF build configuration provides a large number of options.

To ensure that we have all of the required support, we need to build HDF5 and
NetCDF with support for all common requirements, such as FORTRAN, OPENDAP etc.

Therefore, we have collected here the tar files for HDF5, NetCDF and Udunits to
provide a clean build and install. These files are kept up to date as new
versions of these packages become available.

And we include a build and install script which will perform the build in the
correct manner, using configure, and install the packages in your chosen location.

### Choosing where to install

If you need NetCDF support for LROSE only, you can install in places such as:

    $HOME/lrose (this is the default)
    /usr/local/lrose

If you need to support NetCDF for other packages, it makes sense to install in

    /usr/local 

### Tar file location

The tar files are stored in the

    tar_files

subdirectory.

### Performing the build

  * go to the top level directory of this repository.
  * run the `build_and_install_netcdf` script

### Usage

The script takes a single argument:

    build_and_install_netcdf -x target_dir

where `target_dir` defaults to `$HOME/lrose`.

### 32-bit build

If you need to build netcdf and hdf5 libraries that are 32-bit compatible:
  * go to the top level directory of this repository.
  * run the `build_and_install_netcdf.m32` script

For this to work, you will need to install 32-bit versions of the
system libraries.

On Redhat-based hosts you can achieve this by running:

```
yum install -y \
gcc gcc-c++ gcc-gfortran \
glibc-devel.i686 libX11-devel.i686 libXext-devel.i686 \
libtiff-devel.i686 libpng-devel.i686 \
libstdc++-devel.i686 libtiff-devel.i686 \
zlib-devel.i686 expat-devel.i686 flex-devel.i686 \
fftw-devel.i686 bzip2-devel.i686
```

On Debian, you need to run the following:

```
  /usr/bin/dpkg --add-architecture i386
  aptitude update
```

and use apt-get to install the following:

```
  aptitude install libx11-6:i386 \
                   libstdc++-4.9-dev:i386 \
                   libpng12-dev:i386 \
                   libx11-dev:i386 \
                   libxext-dev:i386 \
                   lib32stdc++-4.9-dev \
                   libstdc++5:i386 \
                   libstdc++6:i386 \
                   libxml2:i386 \
                   libgtk2.0-0:i386 \
                   libgdk-pixbuf2.0-0:i386 \
                   libbz2-dev:i386
```

### Usage

The script takes a single argument:

    build_and_install_netcdf -x target_dir

where `target_dir` defaults to `$HOME/lrose`.


