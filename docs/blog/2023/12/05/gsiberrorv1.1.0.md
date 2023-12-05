# GSIBerror V1.1.0

Today I released the GSIBerror V1.1.0 package! The GSIBerror is a Python package aimed to read the records and attributes from the background error covariance matrices compatible with the Gridpoint Statistical Interpolation (in the .gcv file format, global grid).

I made a short video demonstrating the basic function of the package and release it in the [PyPi](https://pypi.org/project/GSIBerror/) as well!

![type:video](https://youtube.com/embed/utEsGoTVE4o)

The usage is very simple:

```python 
import gsiberror as gb

bfile = gb.Berror('gsi_berror_file.gcv')

bfile.read_amplitudes()

bfile.nlat, bfile.nlon, bfile.nlev

bfile.amplitude['sf'].plot.contourf()
```

The documentation of the package is [here](https://gad-dimnt-cptec.github.io/GSIBerror/) and the GitHub repository is [here](https://github.com/GAD-DIMNT-CPTEC/GSIBerror).

Cheers,

cfbasz
