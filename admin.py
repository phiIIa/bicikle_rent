
class Admin:
    def __init__(self, stations, total_revenue):
        self.stations = stations
        self.total_revenue = total_revenue

    def get_station_report(self):
        report = {}
        for station in self.stations:
            report[station.name] = len(station.bicycles)
        return report

    def get_total_revenue(self):
        return self.total_revenue

    def generate_report(self):
        report = self.get_station_report()
        for station, count in report.items():
            print(f"Станція {station}: {count} велосипедів")
        print(f"Загальна виручка: {self.total_revenue} грн")
