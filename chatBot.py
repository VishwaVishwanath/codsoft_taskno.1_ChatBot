import random
import re

class RuleBot:
    ##response
    negative_res = ("no","nope","nah","naw","not a chance","sorry")
    exit_commands = ("quit","pause","exit","goodbye","bye","later")
    
    
    random_question = (
        "why are you here? ",
        "Are there many humans like you? ",
        "what do you consume for sustenance? ",
        "Is there Intelligent life on this planet? ",
        "Does Earth have a Day and Night ? "
    )
    
    def __init__(self):
        self.alienbabble = {
            'describe_planet_intent': r'.*\s*your planet.*',
            'answer_why_intent': r'why\sare.*',
        }
    
    def greet(self):
        print("\n\n\nWelcome to ****Responsive Chat-Bot****\n")
        print("                     -by VISHWANATH\n\n")

        self.name = input("what is your name ?\n")
        will_help = input(
            f"Hi {self.name}, I am Chat-Bot. Will you help me learn about your planet?\n")
        if will_help in self.negative_res:
            print("--> Have nice earth day...!\n")
            return 
        self.chat()
        
    def make_exit(self, reply):
        for command in self.exit_commands:
            if reply == command:
                print("\n   --> Have a nice day...!\n")
                return True

    def chat(self):
        reply = input(random.choice(self.random_question)).lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))
            
    
    def match_reply(self, reply):
        for intent, regex_pattern in self.alienbabble.items():
            found_match = re.match(regex_pattern, reply)
            if found_match and intent == 'describe_planet_intent':
                return self.describe_planet_intent()
            elif found_match and intent == 'answer_why_intent':
                return self.answer_why_intent()
            
        
        if not found_match:
            return self.no_match_intent() 
        
    # Ur planet
    def describe_planet_intent(self):
        responses = ("My planet is Mars, full of Meachines\n",
                    "I heard Chai is goood in Your planet,is it?\n")
        return random.choice(responses)
    
    # why are
    def answer_why_intent(self):
        responses = ("I come in peace \n","I am here to collect data on your planet and its inhabitants\n",
                      "I heard the Chai is good in Your planet,is it?\n")
        return random.choice(responses)
    
    #Rapid-Fire..
    def no_match_intent(self):
        responses = ( "Please tell me more.\n","tell me more!\n","I see.Can you elaborate\n",
                        "Interesting.can you tell me more ?\n","I see.How do you think?\n","why?\n",
                         "How do you think I feel when i say that. Why?\n")
        return random.choice(responses)

bot = RuleBot()
bot.greet()