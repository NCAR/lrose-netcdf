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

    $HOME/lrose
    /usr/local/lrose (this is the default)

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

where `target_dir` defaults to `/usr/local/lrose`.


