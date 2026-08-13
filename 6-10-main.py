from GROQ import generate_response


def reinforcement():
    prompt=input("Enter a prompt").strip()
    if not prompt:
        print("Please enter a prompt to run ")
        return
    init_response=generate_response(prompt, temperature=0.3, max_tokens=1024)
    print(f"\nInit AI responses: {init_response}")
    try:
        rating=int(input("rate the response from 1 to 5:").strip())
        if rating <1 or rating >5:
            print("invalid rating. using 3.")
            rating=3
    except ValueError:
        print("Invalid rating. using 3")
        rating=3
    feedback=input("provide feedback for improv:").strip()
    improved_response=f"{init_response} (imporved with your feedback: {feedback})"
    print(f"imporoved response: {improved_response}")

    print("\nreflection\n\n1. how did the model's response improve with feedback?\n2. how does reinforcement learning help ai to imporove its performance over time?")


def role_based():
    print("role based activity")
    category=input("enter a catefory\n-").strip()
    item=input(f"enter a specific {category} topic").strip()

    if not category or item:
        print("pls fill in bothb fields to run the activity")
        return
    teacher_prompt=f"You are a teacher. explain {item} in simple terms"
    expert_prompt=f"You are an expert in {category}. explain {item} in detailed terms"
    teacher_response=generate_response(teacher_prompt, temperature=0.3, max_tokens=1024)
    expert_response=generate_response(expert_prompt, temperature=0.3, max_tokens=1024)
    print(f"teachers perspective\n\n-{teacher_response}")
    print(f"expert perspective\n\n-{expert_response}")
    print("\n\n\n\n\nreflection\n\n\n\n1. how did the ai's response differ from the teacher and the expert?\n2. how can the role b ased prompts help tailor ai responses for different contexts?")

def run():
    choice=input("choose an activity:\n1. reinforced learning\n2. role-based prompts").strip()
    if choice =="1":
        reinforcement()
    elif choice=="2":
        role_based()
    else:
        print("nuh uh. choose either one or 2.")

if __name__=="__main__":
    run()

