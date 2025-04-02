#### DAY 4

### Detailed Notes and Hands-On Examples for Teaching Teens (13-17)

#### Section 1: Introduction to Teachable Machine

- **What is Teachable Machine?**  
  Teachable Machine is a free, web-based tool created by Google that lets anyone build simple AI models without needing to code. It’s like teaching a computer to recognize patterns—like pictures, sounds, or even text—by giving it examples. Today, we’re going to use it to build a text-based AI that can figure out if a sentence is positive or negative (this is called _sentiment analysis_).
- **Why is this cool?**  
  Imagine you could teach a computer to read movie reviews and tell you if people liked the movie or not. That’s what we’re doing today! Companies use this kind of AI to understand what customers think about their products, and you’re going to learn how it works.

- **How does it work?**  
  Teachable Machine learns by looking at examples you give it. For text, you’ll type in sentences and tell it what they mean (like “happy” or “sad”). Then, it figures out patterns in the words to guess the meaning of new sentences.

**For You (Teacher Explanation):**  
Start with this simple intro to get them excited. Use relatable examples (like movie reviews or social media comments) to show how AI connects to their world. Keep it light and fun—teens this age respond well to hands-on stuff over heavy theory.

#### Section 2: Hands-On Activity – Building a Sentiment Analysis Model

**Notes for Learners:**

- **What is Sentiment Analysis?**  
  Sentiment analysis is when a computer figures out if a piece of text is positive (happy, excited), negative (sad, angry), or neutral (meh, no strong feelings). For example:

  - “I love this game!” = Positive
  - “This homework is the worst.” = Negative
  - “The sky is blue.” = Neutral

- **Let’s Build It!**  
  We’re going to make an AI that can tell if a sentence is positive or negative. Here’s how:

  1. **Go to Teachable Machine:** Open your browser and go to [teachablemachine.withgoogle.com](https://teachablemachine.withgoogle.com/). Click “Get Started.”
  2. **Choose Text Project:** Pick the “Text” option (it’s the one with the “T” icon).
  3. **Set Up Classes:** You’ll see boxes called “classes.” These are the categories your AI will learn. Rename the first box “Positive” and the second box “Negative.”
  4. **Add Examples:** Type sentences into each box. For example:
     - Positive: “This is so much fun!” “I’m super happy today!” “Great job, team!”
     - Negative: “I’m really upset.” “This is boring.” “I don’t like this at all.”
     - Add at least 5-10 sentences per box. The more, the better!
  5. **Train the Model:** Click the “Train Model” button. The computer will study your examples and learn the difference between positive and negative.
  6. **Test It:** After it’s trained, type a new sentence in the “Test” area (like “I’m having a great day!”) and see if it guesses “Positive” or “Negative” correctly.

- **Tips:**
  - Use words you’d see in texts or posts—like “awesome,” “lame,” or “yay.”
  - If it guesses wrong, add more examples to help it learn better.

**Hands-On Example for Learners:**

- **Step-by-Step Challenge:**
  1. Open Teachable Machine and set up your “Positive” and “Negative” classes.
  2. Add these sentences:
     - Positive: “I aced my test!” “This pizza is amazing!” “Can’t wait for the weekend!”
     - Negative: “I lost my phone.” “This rain sucks.” “I’m so tired of this.”
  3. Train the model.
  4. Test it with: “This movie is epic!” and “I hate waiting.” Write down what it guesses!

**For You (Teacher Explanation):**  
Guide them through the steps live on a projector or their own devices. Encourage them to experiment with their own sentences (like stuff they’d text their friends). If they mess up, that’s okay—show them how adding more examples fixes it. This keeps it interactive and shows them AI isn’t perfect right away—it learns like they do!

#### Section 3: Exploring Different Training Datasets

**Notes for Learners:**

- **What’s a Dataset?**  
  A dataset is just a bunch of examples you give the AI to learn from. Think of it like a study guide for a test—the better the guide, the smarter the AI gets. For our sentiment model, the dataset is the sentences we typed in.

- **Why Does It Matter?**  
  If you only give it a few examples, or if they’re all super similar (like “I’m happy” over and over), the AI won’t be very smart. It’s like if you only studied one page of a book for a big test—you’d miss a lot! Good datasets have lots of different examples.

- **Try This:**  
  Let’s mix it up! Add some new sentences to your model and retrain it. For example:

  - Positive: “This song slaps!” “My dog is the best!” “Winning feels so good!”
  - Negative: “My Wi-Fi is trash.” “This game keeps crashing.” “Ugh, Mondays.”
  - Retrain and test again. Did it get better at guessing?

- **Fun Experiment:**  
  Split into pairs. One person adds only short sentences (like “Cool!” or “Bad!”), and the other adds longer ones (like “I’m so excited for the party tonight!” or “I can’t stand this annoying noise.”). Test both models. Which one works better?

**Hands-On Example for Learners:**

- **Dataset Swap:**
  1. Add 5 new sentences to your Positive and Negative classes (use slang or stuff you’d say to friends).
  2. Retrain the model.
  3. Test with: “This is dope!” and “I’m over it.” Did it guess right? Share your results with the group!

**For You (Teacher Explanation):**  
This part teaches them that AI depends on good data. Let them play with different sentence styles (short, long, slangy) to see how it affects the model. It’s a sneaky way to show them “garbage in, garbage out” without boring them with jargon. Keep it a game—whose model guesses best?

#### Section 4: Discussion – Misinformation and Truthful Chatbots

**Notes for Learners:**

- **AI and Misinformation:**  
  AI chatbots (like me, Grok!) can be super helpful, but they can also spread _fake news_ if they’re not built carefully. For example, if someone trains an AI with wrong info—like “the moon is made of cheese”—it might believe that and tell everyone! This happens online a lot with rumors or lies.

- **Real-Life Example:**  
  Imagine an AI reading tons of social media posts saying “This new drink cures colds!” If most posts are fake but the AI doesn’t know, it might tell you it’s true. That’s why people worry about AI-powered chatbots spreading misinformation.

- **How Can We Fix It?**

  - **Good Data:** Train AI with true, checked facts—not just random stuff from the internet.
  - **Double-Checking:** Make AI say “I’m not sure” if it’s guessing, instead of acting like it knows everything.
  - **Human Help:** Have people review what the AI says to catch mistakes.

- **What Do You Think?**
  - Have you seen fake stuff online? How did you know it wasn’t true?
  - How would you make a chatbot you could trust?

**Hands-On Discussion Activity:**

- **Chatbot Detective Game:**
  1. I’ll give you 3 sentences an AI might say. You decide if they sound true or fake:
     - “Cats can live up to 100 years.” (Fake—usually 12-18 years!)
     - “The sun is hot because it’s a big ball of fire.” (Half-true—it’s more about nuclear fusion.)
     - “Video games make you smarter.” (Could be true—some studies say yes, some say no.)
  2. Talk in groups: How could an AI get these wrong? What would you teach it to do better?

**For You (Teacher Explanation):**  
This ties the tech to their lives—teens are online all the time and have seen fake news. Keep the discussion casual but push them to think critically. The game makes it fun while showing how AI can mess up if it’s not trained right. Encourage wild ideas for “fixing” chatbots—they’ll surprise you!

#### Materials Needed

- **Teachable Machine:** Access via [teachablemachine.withgoogle.com](https://teachablemachine.withgoogle.com/) (works on any browser).
- **Sample Text Datasets:** Use the examples above or let them make their own.
- **Tutorial Video:** Google’s quick Teachable Machine intro (search “Teachable Machine Text Tutorial” on YouTube—about 5 minutes) if you want a visual guide.

#### Wrap-Up for Learners

- **What You Learned:**  
  You built an AI that can guess if a sentence is positive or negative! You also saw how the examples you give it (the dataset) make it smarter—or dumber. Plus, we talked about how AI can spread fake news if we’re not careful.

- **Next Steps:**  
  Try testing your model with trickier sentences (like sarcasm—“Wow, great day…” when it’s not). Or make a new model with more categories, like “Happy,” “Sad,” and “Angry.” Keep playing with it!

**For You (Teacher Explanation):**  
End with a quick recap and praise their work—teens love feeling accomplished. Suggest fun follow-ups to keep them curious. If time’s short, skip the sarcasm bit, but it’s a great hook for next time!

This plan is hands-on, teen-friendly, and balances learning with fun. Let me know if you want tweaks or more examples!
