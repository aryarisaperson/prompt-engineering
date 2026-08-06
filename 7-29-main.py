from GROQ import generate_response

import re
import streamlit as ai
def looks_incomplete(text:str) ->bool:
    if not text or len(text.strip()) < 10:
            return True
    t=text.strip()
    if t.endswith(("**", "*", "-", "_", ":", ",", "(", "[", "{")):
            return True
    if re.search(r"\d+\.\s*\*\*$", t):
            return True
    if not re.search(r"[.!?]\s*$", t):
           return True
    return False
def complete_answer(question: str, max_rounds:int=2) ->str:
       base_prompt=(
              "answer clearly in numbered points. "
              "do not cut sentences. Finish each point fully.\n\n"
              f"question: {question}"
       )
       ans=generate_response(base_prompt, temperature=0.3, max_tokens=1024)
       rounds=0
       while rounds < max_rounds and looks_incomplete(ans):
        cont_prompt=(
              "Continue EXACTLY from where you stopped. "
              "Do NOT repeat earlier text. "
              "Finish the incomplete point and complete the answer.\n\n"
              f"question: {question}\n\n"
              f"Answer so far:\n{ans}\n\nContinue:"
       )
        more=generate_response(cont_prompt, temperature=0.3, max_tokens=1024)
        if not more or more.strip() in ans:
              break
        ans=(ans.rstrip() + "\n" + more.lstrip()).strip()
        rounds +=1
        return ans
def main():
      ai.title("ai teacher yay")
      ai.write("ask me stuff")
      input=ai.text_input("ask away:")
      if input:
            ai.write(f"**heres what you wrote:**{input}")
            response=complete_answer(input)
            ai.write("**aight i responded:**")
            ai.markdown(response)
      else:
            ai.info("pls enter a question")

if __name__=="__main__":
      main()
