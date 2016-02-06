# polygon
API REST for adding and retrieving polygons.

## URL

http://lucas-polygon.us-west-2.elasticbeanstalk.com/

## Endpoints (semi-automated docs)

http://lucas-polygon.us-west-2.elasticbeanstalk.com/docs/

## Example using [httpie](https://github.com/jkbrzt/httpie)

    # Add new provider
    http post <URL>/providers/ name='test' email='test@test.test' phone='+543513939393' language='en' currency='usd'

    # Add new polygon
    http --json post localhost:8083/polygons/ name='p10' price=1500 provider='test' polygon:='{"type": "Polygon", "coordinates":[ [[100.0, 0.0], [101.0, 0.0], [101.0, 1.0], [100.0, 1.0], [100.0, 0.0]] ]}'
    
    # Get all polygons that contain the point (only in their bounds, would be nice to properly implement this)
    http localhost:8083/polygons/point/100.0/700.0/
