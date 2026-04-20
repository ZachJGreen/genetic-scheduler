from schedule import Schedule
from Activity import create_initial_population, print_population_summary
def main():

    first_gen = create_initial_population()
    print_population_summary(first_gen)
if __name__ == "__main__":
    main()