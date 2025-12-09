import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
texts=[
    "I want to study","help me study","how to revise","I feel sad","Motivate me","Give me motivation","help me code","coding problem","python help"
]
labels=[
    0,0,0,
    1,1,1,
    2,2,2
]
labels=np.array(labels)
tokenizer=Tokenizer()
tokenizer=fit_on_texts(texts)
vocab_size=len(tokenizer.word_index)+1
sequences=tokenizer texts_to_sequences(texts)
padded=pad_sequences(sequences,padding="post")
model=Sequential()
model.add(Dense(16,activation="relu",input_dim=padded.shape[1]))
model.add(Dense(18,activation="relu"))
model.add(Dense(3,activation="softmax"))
model.compile(optimizer="adam",loss="sparse_categorical_crossentropy",metrics=["accuracy"])
model.fit(padded,labels,epochs=50,verbose=0)
print("Chatbot is ready")
def chatbot(user_input):
    seq=tokenizer.texts_to_sequences([user_input])
    padded_seq=pad_sequences(seq,maxlen=padded.shape[1],padding="post")
    prediction=np.argmax(model.predict(padded_seq),axis=1)[0]
    if prediction==0:
        return "Recommendation:Try making short notes and revise daily"
    elif prediction==1:
        return "Recommendation:You are strong Keep doing it"
    elif prediction==2:
        return "Recommendation:Practise python"
while True:
    user=input("You:")
    if user.lower()=="exit":
        break
    print("Bot:",chatbot(user))