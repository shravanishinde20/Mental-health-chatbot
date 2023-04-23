from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

from chatterbot import ChatBot

from chatterbot.trainers import ListTrainer

bot = ChatBot('chatbot', read_only=False, 
                logic_adapters=[
                    {
                        'import_path':'chatterbot.logic.BestMatch',
                        'default_response':'Invalid query! Please enter a valid query.',
                        'maximum_similarity_threshold':0.90
                      
                    }
                    ])

list_to_train = [
            
            
            "1A",
            "It soundss like you're going through a tough time. It's okay to not be okay.🫂<br> Let's do a fun activity to reduce your depression. <br> Please select one from the options below : <br> 1.a Let's do a guided imagery.<br>1.b Let's do daily affirmation. <br> ",

	        "1.a",
            "Sure! Please find a comfortable and quiet place where you won't be disturbed for the next few minutes. Once you're ready, close your eyes, take a deep breath, and allow yourself to relax.  <br>  Close your eyes and take a deep breath. Imagine standing at the edge of a calm, crystal-clear lake with the sun shining down on you and a gentle breeze blowing through the trees. Listen to the sound of the water lapping against the shore and imagine floating in the water. As you float, imagine any negative thoughts or emotions floating away and feeling a sense of peace and calm washing over you. When you're ready, take one last deep breath and slowly open your eyes. Remember the feeling of peace and calm you experienced and carry it with you throughout your day. <br> <br> Please write the number of any query: <br>Please select one from the options below: <br>  1.a.1 Thank you! That was really very helpful.  <br> 1.a.2 Let's do another guided imagery. ",
            "1.a.1",
            "You're welcome! I hope you're feeling much better now. Sometimes it can help to talk about what's going on and get things off your chest.🫂",
            "1.a.2",
            "Sure! This guided imagery exercise involves closing your eyes and taking a deep breath to imagine yourself standing in front of a beautiful, peaceful garden. As you take in the scenery, you notice that there is a path leading deeper into the garden. As you continue to walk, you notice different areas of the garden, each with its own unique beauty. Finally, you come across a peaceful gazebo with comfortable chairs, where you sit down and take in the beauty of the garden. As you sit there, you feel a sense of calm and relaxation, and your worries and stresses melt away. When ready, take a few deep breaths and gently open your eyes. <br> <br> Please write the number of query: <br> 1.a.1 Thank you! That was really very helpful.",


            "1.b",
            "Sure! Daily affirmations are a wonderful way to cultivate positivity and build self-confidence. Repeat the following affirmations to yourself out loud or silently, whichever feels most comfortable to you:<br>✨ I am worthy of love and respect, and I treat myself and others with kindness. ✨ <br>✨ I am capable of achieving my goals and I trust in my ability to succeed. ✨<br>✨ I am grateful for all the good things in my life, and I focus on the positive. ✨<br>✨ I am strong and resilient, and I can handle whatever challenges come my way. ✨<br> Repeat these affirmations daily, ideally in the morning or before bed, to help cultivate a positive mindset and build self-confidence. Remember to believe in yourself and your ability to achieve your goals and live a fulfilling life. <br> <br> Please write the number of any query:<br> 1.b.1 Thank you! That was really very helpful. <br> 1.b.2 Let's do another set of daily affirmations. ",
            "1.b.1",
            "You're welcome! I hope you're feeling much better now. Sometimes it can help to talk about what's going on and get things off your chest.🫂",
            "1.b.2",
            "Sure, daily affirmations can be a great way to start your day with a positive mindset. Repeat these affirmations to yourself daily, with conviction and belief, and watch as they transform your mindset and your life. <br>✨ I am constantly learning and growing, and I embrace change as an opportunity for growth. ✨<br>✨ I am in control of my thoughts and emotions, and I choose to think positively and feel empowered. ✨<br>✨ I am deserving of happiness and fulfillment, and I actively seek out joy in my life. ✨<br><br> Please write the number of query: <br> 1.b.1 Thank you! That was really very helpful.",
            

    
            
            "2A",
            "I'm sorry to hear that you're feeling sad. It's okay to experience difficult emotions from time to time, and it's important to take care of yourself during those moments.  <br> Let's do a fun activity to lighten up your mood. Please select any one from the options below : <br> 2.a Tell me a joke <br>2.b Recommend a funny YouTube video. <br> ",

            "2.a",
            "Sure, here's a joke to hopefully make you smile- <br> Why did the tomato turn red?🍅 <br> Because it saw the salad dressing!🥗🤭 <br> <br> Please write the number of any query: <br>  2.a.1 Thank you! That was really very helpful.  <br> 2.a.2 Tell me another joke",
            "2.a.1",
            "You're welcome! I hope you're feeling much better now. Sometimes it can help to talk about what's going on and get things off your chest.🫂",
            "2.a.2",
            "Sure, here's a joke to hopefully make you smile- <br>Why do seagulls fly over the sea?🌊 <br> Because if they flew over the bay, they'd be bagels!🥯🤭 <br><br> Please write the number of query: <br> 2.a.1 Thank you! That was really very helpful.",
            
            
            "2.b",
            "Sure, here's a funny YouTube video that you might enjoy: <br> Title: 'Try Not To Laugh Challenge #16' by Markiplier <br> <a href=" ' https://www.youtube.com/watch?v=vC3qJzLwBJg' ">Link</a> <br> In this video, Markiplier attempts to complete a 'Try Not To Laugh Challenge' where he watches and reacts to a series of hilarious clips. His reactions and commentary throughout the video are sure to make you laugh out loud. Give it a watch and see if you can resist the urge to laugh along with him!  <br> <br> Please write the number of any query: <br>  2.b.1 Thank you! That was really very helpful.  <br> 2.b.2 Recommend some other funny YouTube video.",
            "2.b.1",
            "You're welcome! I hope you're feeling much better now. Sometimes it can help to talk about what's going on and get things off your chest.🫂",
            "2.b.2",
            "Sure, here's a funny YouTube video that you might enjoy: <br> Title: 'If Google Was a Guy' by CollegeHumor <br> <a href=" 'https://youtu.be/Cxqca4RQd_M' "> Link</a> <br> In this video, a guy goes to Google's office to ask for help with his search queries. The catch is that Google is portrayed as a person, which leads to some hilarious and absurd situations. The video is a great example of CollegeHumor's unique brand of humor, and it's sure to make you laugh. <br><br> Please write the number of query: <br> 2.b.1 Thank you! That was really very helpful.",
            
            
            
            
            
            "3A",
            "I'm sorry to hear that you're feeling angry. It's normal and healthy to experience emotions, including anger. <br> Let's do a fun activity to reduce your anger. <br> Please select one from the options below : <br> 3.a Let's do a counting exercise.<br> 3.b Let's do deep breathing exercise. <br>",
            
            "3.a",
            "Sure, here's a counting exercise you can try: <br> Find a quiet and comfortable place to sit down. <br>Take a few deep breaths to relax your body and mind. <br> Close your eyes and begin counting backwards from 100 in your mind. <br>With each count, visualize a number or imagine yourself writing the number on a chalkboard or whiteboard. <br>If you lose track or get distracted, start over from 100. <br>Try to keep counting until you reach 0. <br>When you reach 0, take a few deep breaths and slowly open your eyes.<br> <br> Please write the number of any query: <br>  3.a.1 Thank you! That was really very helpful. <br> ",
            "3.a.1",
            "You're welcome! I hope you're feeling much better now. Sometimes it can help to talk about what's going on and get things off your chest.🫂",
            
            
            "3.b",
            "Great, let's do a deep breathing exercise together. Here are the steps: <br> Find a quiet and comfortable place to sit down. <br>Close your eyes and take a few deep breaths to relax your body and mind. <br> Inhale deeply through your nose for a count of 4. <br>Hold your breath for a count of 7. <br>Exhale slowly through your mouth for a count of 8. <br>Repeat steps 3-5 for a total of 4 cycles. <br>After completing the fourth cycle, take a few more deep breaths and slowly open your eyes. <br> <br> Please select one from the options below: <br> 3.b.1 Thank you! That was really very helpful. <br> ",
            "3.b.2",
            "You're welcome! I hope you're feeling much better now. Sometimes it can help to talk about what's going on and get things off your chest.🫂",

            
            
            
            
            "4A",
            "That's great to hear! Let's do a fun activity to keep the positive vibes going. <br> Please select one from the options below : <br> 4.a Tell me a hilarious joke. <br> 4.b Tell me a fun fact.",
            
            
            "4.a",
            "Sure, here's a joke for you: <br> Why couldn't the bicycle stand up by itself?🚲 <br> Because it was two-tired! <br> <br> Please select one from the options below: <br> 4.a.1 Hahaha! That was hilarious.😂 <br> 4.b.2 Tell me another joke.",
            "4.b.1",
            "I'm glad you enjoyed it!😉",
            "4.b.2"
            "Sure, here's another joke for you: <br> Why don't scientists trust atoms?👨🏻‍🔬 <br> Because they make up everything! <br> <br> Please select one from the options below: <br> 4.b.1 Hahaha! That was hilarious.😂",
            
            
            "4.b",
            "Sure, here's a fun fact for you: <br> Did you know that a group of flamingos is called a 'flamboyance'? 🦩 <br> It's a fitting name for these vibrant and colorful birds that are often seen in large flocks standing on one leg. <br> <br> Please select one from the options below <br> 4.b.1 Wow! That was really interesting.🤓 <br> 4.b.2 Tell me another fun fact.",
            "4.b.1",
            "I'm glad you found it interesting!😉",
            "4.b.2",
            "Sure!<br> Did you know that there is a species of jellyfish called the immortal jellyfish? 🪼 This jellyfish is capable of reverting back to its juvenile polyp stage after reaching maturity, effectively allowing it to live forever in theory. <br> <br> Please select one from the options below: <br> 4.b.1 Wow! That was really interesting.🤓",
            
            
            
]
    

# chatterbotCorpusTrainer = ChatterBotCorpusTrainer(bot)
list_trainer = ListTrainer(bot)
list_trainer.train(list_to_train)
# chatterbotCorpusTrainer.train('chatterbot.corpus.english')


def index(request):
    return render(request, 'blog/index.html')

def specific(request):
    return HttpResponse("list")

def getResponse(request):
    userMessage = request.GET.get('userMessage')
    chatResponse = str(bot.get_response(userMessage))
    return HttpResponse(chatResponse)