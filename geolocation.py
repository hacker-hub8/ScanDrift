import requests

class GeoLocation:
    def __init__(self, target):
        self.target = target
        self.api_url = f"http://ip-api.com/json/{target}"

    def fetch_location(self):
        try:
            response = requests.get(self.api_url).json()
            if response["status"] == "success":
                print(f"\n[+] Geolocation Data for {self.target}:")
                print(f"  Country: {response['country']} ({response['countryCode']})")
                print(f"  Region: {response['regionName']}")
                print(f"  City: {response['city']}")
                print(f"  ISP: {response['isp']}")
                print(f"  Organization: {response['org']}")
                print(f"  Latitude: {response['lat']}")
                print(f"  Longitude: {response['lon']}")
                print(f"  Timezone: {response['timezone']}")
            else:
                print(f"[-] Failed to fetch geolocation data: {response['message']}")
        except Exception as e:
            print(f"[-] Error fetching geolocation data: {e}")
