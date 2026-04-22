import sys

from schedule import create_initial_population, sort_population_by_score
from fitness_function import fitness_calculate_final_score
from reproduction_phase import reproduce

def main(generations=100):
    if generations < 1:
        raise ValueError("Generation count must be at least 1.")

    population = create_initial_population()

    for generation in range(1, generations + 1):
        fitness_calculate_final_score(population)
        sorted_gen = sort_population_by_score(population)

        top_score = sorted_gen[0].score
        if generation == 1 or generation == generations or generation % 10 == 0:
            print(f"Generation {generation}: top score = {top_score}")

        if generation == generations:
            break

        top_count = len(sorted_gen) // 2
        if top_count % 2 != 0:
            top_count -= 1

        if top_count < 2:
            print("Population too small to continue reproduction.")
            break

        top_performers = sorted_gen[:top_count]
        population = reproduce(top_performers)

        if not population:
            print("No offspring generated; stopping early.")
            break

    final_sorted = sort_population_by_score(population)
    print(f"Final top score after {generation} generation(s): {final_sorted[0].score}")




if __name__ == "__main__":
    generation_count = 100
    if len(sys.argv) > 1:
        try:
            generation_count = int(sys.argv[1])
        except ValueError as exc:
            raise ValueError("Generation count argument must be an integer.") from exc

    main(generation_count)