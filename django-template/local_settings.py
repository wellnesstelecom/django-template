COMPRESS = True # Developing with compress, rare
#COMPRESS_PRECOMPILERS = (
#    ('text/coffeescript', 'coffee --compile --stdio'),
#    ('text/less', 'lessc {infile} {outfile}'),
#    ('text/sass', 'sass {infile} {outfile}'),
#    ('text/x-scss', 'sass --scss {infile} {outfile}'),
#)
#COMPRESS_CSS_FILTERS = [
#    'compressor.filters.compass.CompassFilter',
#    'compressor.filters.css_default.CssAbsoluteFilter',
#]
CACHES = {
    'default': {
    'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
    'LOCATION': '/var/tmp/django_cache',
    }
}
