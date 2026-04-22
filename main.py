import sys

from schedule import create_initial_population, sort_population_by_score
from schedule import print_schedule
from fitness_function import fitness_calculate_final_score
from reproduction_phase import reproduce

def main(generations=100):
    if generations < 1:
        raise ValueError("Generation count must be at least 1.")

    population = create_initial_population()
    previous_best_fitness = None

    for generation in range(1, generations + 1):
        gen_scores = fitness_calculate_final_score(population)
        if not gen_scores:
            print("No schedules available for fitness evaluation.")
            break

        sorted_gen = sort_population_by_score(population)
        best = sorted_gen[0]
        best_fitness = best.score
        average_fitness = sum(gen_scores) / len(gen_scores)
        worst_fitness = min(gen_scores)

        if previous_best_fitness is None:
            improvement_text = "N/A (first generation)"
        elif previous_best_fitness == 0:
            if best_fitness == 0:
                improvement_text = "0.00%"
            else:
                improvement_text = "inf%"
        else:
            improvement = ((best_fitness - previous_best_fitness) / abs(previous_best_fitness)) * 100
            improvement_text = f"{improvement:.2f}%"

        print(f"\nGeneration {generation} Fitness Matrix")
        print(f"Best fitness: {best_fitness:.2f}")
        print(f"Average fitness: {average_fitness:.2f}")
        print(f"Worst fitness: {worst_fitness:.2f}")
        print(f"Generation-to-generation improvement: {improvement_text}")
        print("Best schedule:")
        print_schedule(best)

        previous_best_fitness = best_fitness

        if generation == generations:
            break

        top_count = len(sorted_gen) // 2
        if top_count % 2 != 0:
            top_count -= 1

        if top_count < 2:
            print("Population too small to continue reproduction.")
            break

        top_performers = sorted_gen[:top_count]
        population = reproduce(top_performers, target_size=len(sorted_gen))

        if not population:
            print("No offspring generated; stopping early.")
            break

    final_sorted = sort_population_by_score(population)
    best = final_sorted[0]
    print(f"\nFinal best score after {generation} generation(s): {best.score:.2f}")




if __name__ == "__main__":
    generation_count = 100
    if len(sys.argv) > 1:
        try:
            generation_count = int(sys.argv[1])
        except ValueError as exc:
            raise ValueError("Generation count argument must be an integer.") from exc

    main(generation_count)