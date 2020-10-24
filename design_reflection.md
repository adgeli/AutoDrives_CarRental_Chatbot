# Design Reflection: Sali - AutoDrives Autonomous Car Booking Chatbot

![intro_img](images/Infographic_Design_Process.png)

*The following respository contains the design reflection for the CCT461 Speculative Design course at the University of Toronto Mississauga.*

By: Alexandra Dumitras-Geli, Jennifer Palfi, Melanie Zaky, & Nicole Stafferie

---

# The Design Process that Lead to Sali 

![sali](images/future_driving.jpg)

## Objective

**Insert project summary here**

---

## Document Overview 

- [Background](#Background)
    - [The Problem](#The-Problem)
    - [Research](#Research)
    - [Project Direction](#Project-Direction)

- [Prototyping & Validation](#Prototyping-&-Validation)
    - [Utterances](#Utterances)
    - [Slots & Intents](#Slots-&-Intents)
    - [Buttons](#Buttons)
    - [Code Development: Lambda](#Code-Development:-Lambda-Function) 

- [Postmortem](#Postmortem)
    - [Evaluation](#Evaluation) 
    - [Conclusion](#Conclusion) 
    - [Future Directions](#Future-Directions) 

---

## Background

<img src="images/selfdriving.png" width="750"/>

### The Problem 

The world of driving is changing significantly. Manually operating vehicles is a concept of the past as we move into an era of autonomous, self-driving cars. Thus, just because the method of driving is changing, doesn’t mean people will have less destinations, or places to be. In fact, it might even increase. It is then worth questioning, if people aren’t driving their cars themselves anymore, would they need to own a car? Could there be an autonomous car rental system to cater to this?

    How might we build a chatbot to help people book an autonomous vehicle?

### Research 

There is extensive research by numerous scholars who have studied the trends, impacts and evident future of autonomous vehicles. One study conducted by Fagnant and Kockelman mentions how having an increasing number of autonomous vehicles on the road will not only improve traffic but is predicted to cause less car-accidents (Fagnant & Kockelman, 2014). In addition, with an increased use of autonomous vehicles comes a decrease in emissions released from gas-powered vehicles into our atmosphere, helping tackle global warming (Fagnant & Kockelman, 2014).  It is the positive social and environmental impacts that will be a driving force in consumers adopting autonomous cars into their daily lives (Sparrow & Howard, 2017). Ensuring that the autonomous cars are built with the passenger’s safety as priority will also be a determining factor in the adoption rate (2017). Thus, helping to foresee how far (or close) into the future we are to having a society driven by autonomous vehicles (2017). There was a study conducted by Bansal and Kockelman in 2017 forecasting the long-term adoption rate of autonomous vehicles by Americans. It was found that up to 87% of Americans in the study would be willing to adopt and purchase an autonomous vehicle by 2045, a significant determinant was increasing prices in purchasing (Bansal & Kockelman, 2017). Thus, with all this in mind, it is recognizable that autonomous cars is a future trend we all must prepare to adapt to in some shape or form.

**Ideation:** 

![mood_board](images/mood_board.png)

Chatbots are an ever-increasing technology implemented by many web administrators to. perform tasks and generate conversations with users (Reshmi & Balakrishnan, 2018). By implementing them into a business, companies are able to save on customer service centres, while improving both efficiency of operations (able to work with more than one client at a time) and improving customer support (2018). In order for chatbots to work efficiently and gain sufficient user response is to ensure there is the element of trust established between the virtual assistant and the user (Zhou, Mark, Li & Yang, 2019). This can be formed by the chatbot bringing personal human-like elements into the conversation such as a name and friendly introducing statement (Zhou, Mark, Li & Yand, 2019). If done correctly, chatbots can power the future of business and help increase productivity in many industries (Reshmi & Balakrishnan, 2018). 
Thus, following the research above, created a chatbot that would help users book an autonomous vehicle is practically a seamless fit. 

### Project Direction 

![brainstorm](images/brainstorm.png)

**We agreed that we wanted a chatbot that would:**
- Accomplish the entire booking process for users seeking to book an autonomous vehicle.
- Design a flow of questions that was conversational and simple to follow.
- Create an excellent, personalized customer experience leaving no questions unanswered.

---

## Prototyping & Validation 

**Process Flow:**

![process_flow](images/process_flow.png)

### Utterances 

**Utterance Creation:**

![round_1_utterance](images/Utterances/round1_sampleutterances.png)

Utterances are the first step of the design process. Utterances are phrases, statements of words that the user will input in some sort of sequence. In the case of this chatbot, an example is if the user types “make a car reservation”. This utterance is very broad, however because Amazon LEX uses deep learning it is able to read and register what the user is asking. The more utterances used the better of a chance that amazon LEX will be able to recognize what the user is asking. In terms of what worked, the below images are the utterances we decided to go with. We decided on these through trial and error of what the chatbot responded to, making sure they weren’t too specific that the user wouldn’t type it, but also not too general for amazon to not be able to recognize the request. 

**Utterances in Stage 3 of the Design Process:**

![round_3_utterances](images/Utterances/round3_sampleutterances.png)

### Slots & Intents 

 Intent slots are essentially the action the user wants to do. This is the question that amazon LEX will ask the user. The intent is an overview of the question at a high level. 

 **Intent being asked: What kind of vehicle would you like to rent?**

 ![edit_slot](images/Intents_and_Slots/car_intent_slot_type_1.png)
 
 These intents are important because it is how the bot will respond to inputs from the user and make sure that the questions are flowing in conversation for the user. At this stage it was really about figuring out the conversation flow and making sure the questions were clear to the user, but also that if the user didn’t input the correct answer or follow previous steps that the chatbot was able to recover. 

 **Slots & Intents Editing Process**

 ![edit_slot](images/Intents_and_Slots/editing_slot_types_1.png)
 
 For example, a part of booking an autonomous vehicle is the user has to be over the age of 21 (driver age- slots or intents). What happens if they’re under the age of 21? The chatbot obviously has to recognize this because they are too young to operate a vehicle. Recovering simply means that the chatbot recognizes the birthday is not valid and asks the user to try again. In terms of what worked at this stage it was again just trial and error of working with the conversation flow and chat the chatbot responds to. When there was an error at this stage, we used a code hook to offset said error. 

**Slots & Intents Progress**

![progress](images/Intents_and_Slots/Slot_Type_Progress.png)

### Buttons

**Creating Buttons**

<img src="images/Buttons/Creating_Buttons_1.png" width="425"/> <img src="images/Buttons/Recreating_Buttons.png" width="425"/> 

The buttons part of the design process consisted of selecting multiple choice questions for the user pertaining to the vehicle rental. There was no right or wrong in terms of buttons, it was more so about determining what information we wanted the chatbot to request and what options we wanted to make available to the user. The buttons options are shown below. 

### Code Development: Lambda Function 

**Initializing Environments & Variables:**

<img src="images/code_development/initializing_code.png" width="425"/> <img src="images/code_development/defining_validation_functions.png" width="425"/> 


The most important part of the design process was coding the lambda function. A lambda function is the business logic or context behind the amazon lex chatbot. A User makes a request, and that request could be something like- selecting a vehicle type. Amazon lex then reads the request and sends it over to the lambda function. 

**Validating Intents & the Business Logic**

<img src="images/code_development/defining_intents.png" width="425"/> <img src="images/code_development/lambda_business_logic.png" width="425"/> 

In this function there is a block of code telling the chatbot what to do based on the value inputted. Lambda function is the development process- not just about creating a GUI (user interface) it’s about creating a code that gives business context to the chatbot (lambda). We decided on the results through user testing. Essentially, we kept testing to see how the user responds as well as how the chatbot responds to the user request inputs. 

---

## Postmortem 

<img src="images/driving.jpg" width="700"/> 

### Evaluation 

After a long process of prototyping and evaluating the best format and sequence of questions to be asked, the final product of the chatbot was developed. The initial chat prototype created was increasingly dry in content. The questions were not straight forward and lacked detail. This was an issue as it had the potential to confuse users and make the booking process a tedious one. Therefore, to improve the user’s experience, the questions had to be formulated in a more proficient manner. Within the final prototype, we decided that to be as efficient as possible, we had to first outline the booking process and then develop the questions that would fulfill that. We decided to start off the chatbot booking process with a greeting to make the user experience feel more personal and authentic. 

<img src="images/FINAL_CHAT/FINAL_CHAT_1.png" width="425"/> <img src="images/FINAL_CHAT/FINAL_CHAT_2.png" width="425"/> 

This would mimic the tone of a customer service representative. From there, we then wanted the chatbot to ask some questions regarding the users’ identity for verification purposes, such as their birth date. If the user is of age, the chatbot is to then ask the user questions regarding the specifications of their trip, including the duration, number of passengers, car preference and desired arrival time. The chatbot comes to an end by asking the user if they would like to finalize the booking process and if so, provide them with all the necessary information regarding the details of their booking. Knowing the content, we wanted to include for the booking process made it easier to formulate the questions in a strategic and efficient manner. 

<img src="images/FINAL_CHAT/FINAL_CHAT_3.png" width="425"/> <img src="images/FINAL_CHAT/FINAL_CHAT_4.png" width="425"/> 

From there, we developed a series of twelve questions. To avoid confusion in answers, we made sure to include options in the questions for users to choose from when possible, or questions that would result in a specific answer that could be easily interpreted by the chatbot. In the case where an answer could not be interpreted, the user receives a message stating that the bot was unable to understand the request and to try to better formulate the answer. With that being said, we were aware that users could potentially use different utterances to answer the questions. 

<img src="images/FINAL_CHAT/FINAL_CHAT_5.png" width="300"/> <img src="images/FINAL_CHAT/FINAL_CHAT_6.png" width="300"/> <img src="images/FINAL_CHAT/FINAL_CHAT_7.png" width="300"/> 

Therefore, as we progressed in this final stage of prototyping, we added different variations of utterances to ensure the deep learning algorithm that Sali uses would be able to make more connections to different key phrases a user inputs. For instance, in the first prototype, using utterances that were too similar to each other would trigger an error. But, upon expanding the potential utterances that could be used, even if a user were to input “make a car reservation” instead of “make a vehicle reservation”, Sali is still able to recognize what the user is attempting to input. Furthermore, the use of lambda makes it possible for Sali to have a robust conversation with the user. Lambda essentially delegates a JSON response to Sali with the expected user response (purpose: provide Sali with the logic by having lambda provide what the next steps are for Sali). With those being our prominent strengths, there is also an evident weakness. Specifically, although we expanded the utterances that could potentially be used by the users, some phrasing is still unrecognizable by the chatbot. The chance of this happening could be decreased by adding even more utterance variations; which is possible with more time. An additional feature that could have also been implemented, having had more time and greater skills, is the ability to have users send a picture of their identification in order for Sali to evaluate the validity of their identity and age. 

### Conclusion 

<img src="images/FINAL_CHAT/FINAL_CHAT_8.png" width="425"/> <img src="images/FINAL_CHAT/FINAL_CHAT_9.png" width="425"/> 

In conclusion, as self-driving vehicles continue to become more innovative, the demand for them will also increase. Through extensive research on the uprise of autonomous cars, we decided that developing an autonomous vehicle service can provide consumers with convenience for their everyday initiatives. Unlike uber, this autonomous vehicle service gives users freedom in accessibility throughout the whole duration of their trip. This service is especially convenient as it saves users from the hassle of driving and parking in busy areas in and around the GTA. To make this a simple process, we wanted to develop a chatbot that was straightforward and not time consuming. Therefore, the chatbot went through several testing periods to make sure it focused on customers’ needs and was effective in communication. We developed questions to identify users’ identity and trip details. We made sure to make these questions as simple as possible, without the need of variation in answers. In terms of the technical aspects, we incorporated utterances, intent and slots, buttons and the lambda functionality. These are all factors which make the user experience more proficient.


### Future Directions 

<img src="images/autonomous_car.jpg" width="750"/>

Once the chatbot has gone through a customer testing period to make sure that it adhered to all the customer’s needs and is effective in communicating and booking the services on behalf of the customer, we would be looking to expand to all mobile platforms. Currently the chatbot is only available on the AutoDrives.ca website however to make our services more accessible and convenient we would be looking to develop it into an app. Our end goal would be to offer our service app on both apple and android platforms, as well as on the website so that our services are accessible to everyone whether that be on their mobile or desktop computers. By making our service so accessible we hope that it gives us a competitive advantage over competitors in the autonomous driving industry.

---

