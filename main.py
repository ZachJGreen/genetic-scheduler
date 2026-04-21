from schedule import create_initial_population, print_population_summary, sort_population_by_score
from fitness_function import fitness_calculate_final_score
def main():

    # Initial Population Creation
    first_gen = create_initial_population()

    # Calculate Fitness Scores for the Initial Population
    gen_scores = fitness_calculate_final_score(first_gen)

    # Sort the population by score to identify the best schedules
    sorted_gen = sort_population_by_score(first_gen)
    
    # Take the top 50% of the population for the next generation
    top_performers = sorted_gen[: len(sorted_gen) // 2]

    print_population_summary(first_gen)

    for score in gen_scores:
        print(score)

    print(f"Top schedule score: {sorted_gen[0].score}")




if __name__ == "__main__":
    main()