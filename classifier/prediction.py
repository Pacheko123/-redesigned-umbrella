import pickle


class Predict:

    # function to run for prediction
    def detecting_fake_news(self, item):
        # retrieving the best model for prediction call
        load_model = pickle.load(open('./classifier/final_model.sav', 'rb'))
        prediction = load_model.predict([item])
        prob = load_model.predict_proba([item])
        print("The given statement is ", prediction[0])
        print("The truth probability score is ", prob[0][1])
        return prediction[0], prob[0][1]
