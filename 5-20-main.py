from GROQ import generate_response

def run_activity():
    print("zero shot, one shot, and few shot")
    category=input("enter a category:").strip()
    item=input(f"enter a specific category {category} to classify")
    if not category or not item:
        print("pls fill in both fields to run the activity")
        return
    zero_shot=f"is {item} in a {category}? y/n"
    print("\nzero shot learning yayyayayaa")
    print(zero_shot)
    print(f"response: {generate_response(zero_shot, temperature=0.3, max_tokens=1024)}")

    one_shot=f"example: \ncategory=fruit\nitem=apple\nanswer= ya bro\n\nnow you try:\ncategory= {category}\nitem= {item} answer:"
    print("one shot learning yayayayaayayaya")
    print(f"response: {generate_response(one_shot, temperature=0.3,max_tokens=1024)}")

    creative_prompt=f"write a one sentence story about the given word.\n example: word:moon\nstory: the moon winked at the lovers as they shared their first kiss\nword: {item}\nstory:"
    print(f"few shot: {creative_prompt}")
    print(f"response: {generate_response(creative_prompt, temperature=0.7,max_tokens=1024)}")

    user_prompt=input("Now you try\n-")
    temp=input("put temperature\n-")
    print(f"response: {generate_response(user_prompt, temperature=temp,max_tokens=1024)}")
    print("reflection questions")
    print("1. how did the responses differ between zero shot, oneshot, and freeshot")
    print("2. which approach gave the most helpful response?")
    print("3. how did the example influence the model's output")

if __name__ == "__main__":
    run_activity()