
from voyager_x.spacecraft import Spacecraft

def main():
    voyager = Spacecraft("VOYAGER-X")

    voyager.initialize()

    telemetry = voyager.get_telemetry()

    print("\n--- SPACECRAFT TELEMETRY ---")

    for key, value in telemetry.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
