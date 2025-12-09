from datetime import datetime
from .base import ProviderBase

class MockProvider(ProviderBase):
    """Returns deterministic mock data for resorts and conditions."""
    def fetch_resorts(self):
        return [
            {
                'external_id': 'alpine-summit',
                'name': 'Alpine Summit',
                'location': 'Mountain Valley',
                'lat': 45.0,
                'lng': -120.0,
                'opens': '08:00',
                'closes': '16:00',
                'total_runs': 20,
            },
            {
                'external_id': 'snowway-peaks',
                'name': 'Snowway Peaks',
                'location': 'North Ridge',
                'lat': 46.0,
                'lng': -121.0,
                'opens': '09:00',
                'closes': '17:00',
                'total_runs': 15,
            },
        ]

    def fetch_conditions(self, resort_external_id: str = None):
        now = datetime.utcnow()
        data = [
            {'external_id': 'alpine-summit', 'temperature_c': -5.0, 'snow_depth_cm': 120.0, 'status': 'open', 'observed_at': now},
            {'external_id': 'snowway-peaks', 'temperature_c': -2.3, 'snow_depth_cm': 85.0, 'status': 'open', 'observed_at': now},
        ]
        if resort_external_id:
            return [d for d in data if d['external_id'] == resort_external_id]
        return data

