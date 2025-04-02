## Introduction to Artificial Intelligence and Machine Learning

## Introduction to Teachable Machine

## Objectives:

Students will be able to define basic concepts related to Machine Learning. Students will be able to navigate the Teachable Machine interface. Students will be able to create a simple image classification model using Teachable Machine. Students will be able to test and improve the accuracy of their models. Students will be able to discuss the ethical implications of AI-powered image recognition.

## Materials:

Computers with internet access Teachable Machine website (https://teachablemachine.withgoogle.com/) Webcams (if available; optional) Various objects for image classification (e.g., fruits, toys, school supplies) Teachable Machine tutorial video (link provided in lesson procedure) Whiteboard or projector

## Lesson Procedure:

# Part 1: Introduction to Machine Learning (20 minutes)

Icebreaker/Engagement (5 minutes): Begin by asking students if they’ve ever interacted with AI (e.g., Siri, Alexa, image recognition on their phones). Discuss what AI is and where they see it in their daily lives.

# Defining Machine Learning (10 minutes):

Explain that Machine Learning is a type of AI that allows computers to learn from data without being explicitly programmed. Use analogies relevant to their age group. For example: “Think of it like teaching a dog a trick. You show them what you want them to do, reward them when they get it right, and correct them when they get it wrong. Machine learning is similar – we show the computer lots of examples, and it learns to recognize patterns.” Introduce the concept of “training data.” Explain that the more data you give a machine learning model, the better it becomes at making predictions. Briefly touch on different types of machine learning (supervised, unsupervised, reinforcement learning), but focus on supervised learning as it’s relevant to Teachable Machine.

# Introducing Teachable Machine (5 minutes):

Explain that Teachable Machine is a user-friendly web-based tool that allows anyone to create machine learning models without coding. Highlight its accessibility and ease of use for beginners. Mention that they will be creating an image classification model today.
Part 2: Demonstration of Teachable Machine (30 minutes)

# Accessing Teachable Machine (2 minutes):

Have students open their web browsers and navigate to https://teachablemachine.withgoogle.com/. Ensure everyone can access the site.

# Interface Walkthrough (15 minutes):

Project the Teachable Machine interface on the whiteboard or screen. Step-by-Step Demonstration:Project Type: Explain the different project types (Image Project, Audio Project, Pose Project). For this lesson, select “Image Project” and then “Standard Image Model”. Classes: Explain the concept of “classes.” Each class represents a different category the model will learn to recognize. Demonstrate how to rename the default classes (e.g., Class 1 to “Apple”, Class 2 to “Banana”). Show how to add more classes if needed. Input Methods: Demonstrate how to add images to each class using both the webcam and uploading from files. Explain when they might use each method. Training: Explain the purpose of the “Train Your Model” button. Emphasize that the model learns from the images they provide. Preview: Show how to use the “Preview” section to test the model with new images. Export: Briefly mention the “Export Model” function, explaining that they can export the trained model to use in other projects.

# Tutorial Video (13 minutes):

Show a short, engaging tutorial video on Teachable Machine. (Search on YouTube for “Teachable Machine Tutorial for Beginners” - choose a video that is 5-10 minutes long and clearly explains the basic steps.) Pause the video at key points to reinforce the concepts and answer questions.

## Part 3: Hands-on Activity: Creating an Image Classification Model (50 minutes)

# Choosing Objects (5 minutes):

Have students gather various objects to use for their image classification model. Encourage them to choose objects that are visually distinct (e.g., a red apple, a blue pen, a green leaf). Alternatively, provide a set of objects for students to use.
Creating Classes and Training the Model (30 minutes):
Instruct students to create a new Image Project in Teachable Machine. Guide them through the process of creating classes for each of their chosen objects. Remind them to provide a sufficient number of images for each class. Encourage them to take pictures from different angles and in different lighting conditions. Explain why this is important for model accuracy. Once they have collected their images, have them click the “Train Your Model” button. Explain that the training process may take a few minutes.

# Testing and Improving the Model (15 minutes):

Once the model is trained, have students use the “Preview” section to test its accuracy. Encourage them to try different images and see if the model correctly identifies the objects. If the model is not accurate, guide them to add more training data or adjust the existing data. Explain that the more data they provide, the better the model will become. Ask them to consider what might be causing the model to misclassify certain objects. (e.g., similar colors, unusual angles).

# Part 4: Discussion: Ethical Implications of AI (20 minutes)

## Introduction to Teachable Machine

# What is Teachable Machine?

Teachable Machine is a web-based tool developed by Google that allows users to train machine learning models without needing to write code. It enables anyone to create models for image, audio, and pose classification in an easy and interactive way.

# Why is Teachable Machine Important?

- It helps understand how AI works in a simple and interactive way.
- It allows students to experiment with AI without needing advanced programming knowledge.
- It can be used for practical applications like recognizing objects, identifying sounds, and understanding human gestures.

## Teachable Machine Interface and Features

# Step 1: Accessing Teachable Machine

- Open a web browser and go to Teachable Machine.
- Choose the type of model to train:
- Image Project (for recognizing objects, faces, or handwritten text)
- Audio Project (for recognizing different sounds or words)
- Pose Project (for recognizing body movements)

# Step 2: Understanding the Interface

- Training Panel: Allows users to upload images or capture them with a webcam.
- Classes: These represent categories you want the AI to recognize.
- Training Button: Used to train the model based on provided examples.
- Preview Panel: Shows real-time predictions after training.
- Export Options: Enables you to download or use the model in other applications.
- Hands-on Activity: Creating a Simple Image Classification Model
- Objective: Train an AI model to recognize different objects (e.g., book, pen, and bottle).

# Step 1: Setting Up the Project

- Click "Get Started" on Teachable Machine.
- Select "Image Project" and choose "Standard Image Model".

# Step 2: Collecting Training Data

- Create three classes (e.g., "Book", "Pen", "Bottle").
- For each class:
- Use the webcam or upload at least 20 images of the object from different angles and lighting conditions.
- Ensure variation in the background to make the model robust.

# Step 3: Training the Model

- Click "Train Model" and wait for the system to process the data.
- After training, test the model using real objects or images it has never seen before.

# Step 4: Improving the Model

- If the model misclassifies an object:
- Add more images with different angles and lighting.
- Remove incorrect or unclear images.
- Retrain the model and test again.
- Testing and Deploying the Model

# Step 1: Testing the Model

- Hold up an object in front of the webcam and observe the classification results.
- Check the confidence level of the predictions.
- Identify areas where the model struggles and refine the training data.

# Step 2: Exporting the Model

- Click on "Export Model".
- Choose "TensorFlow.js" (for web-based applications) or "TensorFlow Lite" (for mobile apps).
- You can integrate the model into websites or apps for further use.
- Discussion: Ethical Considerations in AI-Powered Image Recognition
- Potential Misuse of AI Image Recognition
- Surveillance: AI-powered cameras can track people’s movements without consent.
- Bias and Discrimination: AI models might misclassify people based on biased training data.
- Privacy Concerns: Collecting and storing images may lead to privacy breaches.

# How to Prevent Misuse?

- Transparency: Inform people when AI is being used.
- Diverse Training Data: Train models with diverse images to avoid biases.
- Ethical AI Use Policies: Ensure AI tools are used responsibly by governments and companies.
- User Consent: Always seek permission before capturing or analyzing people’s images.

# Conclusion

- Teachable Machine is a powerful and easy-to-use tool for understanding AI.
- Hands-on practice helps students see how AI learns and makes predictions.
- Ethical considerations should always be part of AI development and usage.
- By following these steps, students will gain hands-on experience with AI and understand both its capabilities and limitations in the real world.
