# gps_test.py – Retrieves GPS data using gpsd

import gps

def get_gps_data():
    session = gps.gps(mode=gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
    for _ in range(10):
        report = session.next()
        if report['class'] == 'TPV':
            if hasattr(report, 'lat') and hasattr(report, 'lon'):
                return f"{report.lat},{report.lon}"
    return None

if __name__ == "__main__":
    print("Waiting for GPS fix...")
    location = get_gps_data()
    if location:
        print(f"Location: {location}")
    else:
        print("No fix.")
