import cdsapi

c = cdsapi.Client()

c.retrieve(
    'seasonal-original-single-levels',
    {
        'format': 'netcdf',
        'originating_centre': 'ecmwf',
        'system': '51',
        'variable': 'total_precipitation',
        'year': '2024',
        'month': '04',
        'day': '01',
        'leadtime_hour': [
            '5112', '5136', '5160',
        ],
        'area': [
            40, 70, 5,
            100,
        ],
    },
    'download.nc')
