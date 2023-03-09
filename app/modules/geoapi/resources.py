# encoding: utf-8

"""
RESTful API GeoAPI resources
--------------------------
"""

from flask import request, jsonify
from flask_restx import Namespace, Resource, abort
from flask_restx import fields
from http import HTTPStatus
from shapely.geometry import Polygon, shape
from app.modules.geoapi import GeoApiNamespace


api = Namespace('geoapi', description=GeoApiNamespace.description)

bounding_box = api.model('BoundingBox', {
    'x_lat': fields.Float(),
    'y_lat': fields.Float(),
    'x_lng': fields.Float(),
    'y_lng': fields.Float(),
})

# API modules
polygon = api.model('PolygonGeometry', {
    'type': fields.String(required=True, default="Polygon"),
    'coordinates': fields.List(fields.List(fields.Float, required=True, type="Array"),
                               required=True, type="Array")
})

polygon_feature = api.model('PolygonFeature', {
    'type': fields.String(default="Feature", require=True),
    'properties': fields.String(required=False),
    'geometry': fields.Nested(polygon, required=True)
})

polygon_collection = api.model('FeatureCollection', {
    'type': fields.String(default="FeatureCollection", require=True),
    'features': fields.Nested(polygon_feature, required=True)
})

#API POST method and route
@api.route('/polygon/intersect/')
class PolygonIntersect(Resource):
    """
    Return boolean value based on the intersection of two polygons
    """

    @api.expect(polygon_collection)
    @api.doc(id='polygon_intersect', validate=True)
    def post(self):
        """
        Return boolean value based on the intersection of two polygons
        """
        try:
            #geojson payload to json format
            data = request.get_json()
            # print(data)

            # Get features from JSON request
            poly1 = data['features'][0]
            poly2 = data['features'][1]

            # Get geometries from features
            pol1 = poly1['geometry']
            pol2 = poly2['geometry']

            # Parse coordinates from features
            # coords1 = poly1['geometry']['coordinates']
            # coords2 = poly2['geometry']['coordinates']

            # Convert the geometries to the appropriate format (tuple)
            Polygon1 = shape(pol1)
            Polygon2 = shape(pol2)

            # Perform intersection analysis
            result = Polygon1.intersects(Polygon2)
            print(result)

            # Print boolean result
            return jsonify({'Result' : result})
            # return print(Polygon1.intersects(Polygon2))
        except Exception as err:
            abort(HTTPStatus.UNPROCESSABLE_ENTITY, message="The GeoJSON polygon couldn't be processed.", error=err)

