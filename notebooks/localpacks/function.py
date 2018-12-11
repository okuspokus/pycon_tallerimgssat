import matplotlib.pyplot as plt
import numpy as np

#para crear un STACK y un CLIP
import gdal 

def firmas_teo():
    # Muchos de estos datos los pude obtener gracias a Maira Gayol, muchas gracias!
    x = [1,2,3,4,5,6]
    plt.plot(x,[0.03,0.05,0.04,0.4,0.14,0.07],color='g',label='vegetacion densa',marker='o')
    plt.plot(x,[0.03,0.05,0.04,0.27,0.12,0.07],color='g',label='vegetacion no densa',marker='o')

    plt.plot(x,[0.05,0.11,0.13,0.06,0.02,0.01],color='brown',label='agua turbia',marker='o')
    plt.plot(x,[0.03,0.04,0.035,0.05,0.02,0.01],color='b',label='agua clara',marker='o')
    plt.plot(x,[ 0.10, 0.13, 0.15, 0.26, 0.25, 0.21],color='gray',label='ciudad',marker='o')
    #plt.plot(x,[4,3,2,5],color='b',label='vegetacion')
    plt.ylim(0.0,0.5)
    plt.legend()
    plt.xticks(np.arange(1,7),('Blue','Green','Red','NIR','SWIR1','SWIR2'))
    plt.xlabel('Bandas')
    plt.ylabel('Reflectancia')


def array2raster_1band(out_name,array,geo_trans,proj):
    # https://pcjericks.github.io/py-gdalogr-cookbook/raster_layers.html
    # http://blog.remotesensing.io/2013/03/using-gdal-with-python-basic-intro/

    # First of all, gather some information from the original file
    cols,rows = array.shape
    trans       = geo_trans
    proj        = proj
    #nodatav     = data.GetNoDataValue()
    outfile     = out_name

    # Create the file, using the information from the original file
    outdriver = gdal.GetDriverByName("GTiff")
    outdata   = outdriver.Create(str(outfile), rows, cols, 1, gdal.GDT_Float32)

    # Georeference the image
    outdata.SetGeoTransform(trans)

    # Write projection information
    outdata.SetProjection(proj)

    band = outdata.GetRasterBand(1)
    band.WriteArray(array)
    band.FlushCache()
    

def array2raster(out_name,array,geo_trans,proj):
    # First of all, gather some information from the original file
    cols,rows,bands = array.shape



    # Create the file, using the information from the original file
    outdriver = gdal.GetDriverByName("GTiff")
    
    outfile = out_name #¿ESTO IRA AQUI?
    
    outdata   = outdriver.Create(str(outfile), rows, cols, bands, gdal.GDT_Float32)


    # Georeference the image
    outdata.SetGeoTransform(trans)

    # Write projection information
    outdata.SetProjection(proj)


    for i in range(1,4):
        band = outdata.GetRasterBand(i)
        band.WriteArray(array[i-1,:,:])
        band.FlushCache()