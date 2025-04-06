from openai_agent import get_agent_response
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)


def main():

    print("\n\n***************************************************************")
    print("*                                                             *")
    print("*         Welcome to the Customer Support AI Agent!!          *")
    print("*                                                             *")
    print("***************************************************************")
    print("\nYou can ask questions about products, policies, and more.")
    print("Type 'exit' to quit the program.\n")
    
    while True:
        user_input = input(Fore.CYAN + "\nQuestion: " + Style.RESET_ALL)
        if user_input.lower() == 'exit':
            print(Fore.RED + "Goodbye!" + Style.RESET_ALL)
            break
        
        # Get the response from the agent
        answer = get_agent_response(user_input)
        
        # Display the response
        print(Fore.GREEN + "\nResponse: " + Style.RESET_ALL + answer)

if __name__ == "__main__":
    main()