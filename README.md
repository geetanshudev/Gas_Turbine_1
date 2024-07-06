# Gas_Turbine_1


![GAS1 (2)](https://github.com/geetanshudev/Gas_Turbine_1/assets/119582068/d12f6135-4252-4336-a2d2-c6a98e20e34b)
<br>
![GAS1 (1)](https://github.com/geetanshudev/Gas_Turbine_1/assets/119582068/43323784-e3ad-4aa5-919c-6899831ca9d3)
<br>
![GAS1 (4)](https://github.com/geetanshudev/Gas_Turbine_1/assets/119582068/f6a4899d-575e-4f57-8f8b-8ae15fc36ba9)
<br>
<br>
<br>


**Gas Turbine Anomaly Prediction**

This repository provides a suite of machine learning models for predicting Nitrogen Oxide (NOx) and Carbon Monoxide (CO) emissions, along with anomaly detection capabilities for both pollutants in a gas turbine system.

**Contents**

* `models.zip`: Compressed file containing pre-trained machine learning models:
    * `pred_model_nox.pkl`: BaggingRegressor model for NOx prediction.
    * `pred_model_co.pkl`: BaggingRegressor model for CO prediction.
    * `class_model_nox.pkl`: BaggingClassifier model for NOx anomaly detection.
    * `class_model_co.pkl`: BaggingClassifier model for CO anomaly detection.
* `app.py`: Flask application to take user input, predict NOx and CO emissions, and detect anomalies.
* `requirements.txt`: Text file listing required Python libraries.

**Getting Started**

1. **Download and Unzip:**
   - Download the repository ZIP file.
   - Unzip the downloaded file to extract the repository contents.

2. **Install Dependencies:**
   - Open a terminal or command prompt in the extracted directory.
   - Install the required Python libraries from requiremnets.txt
   ```bash
   pip install -r requirements.txt
   ```

**Running the Application**

1. **Start the Flask App:**
   - In the terminal, navigate to the directory containing `app.py`.
   - Run the Flask application with this command
     ```bash
     python app.py
     ```

2. **User Interaction:**
   - The Flask app will typically start on `http://127.0.0.1:5000/` (localhost port 5000). Access it in your web browser.
   - The web interface should provide input fields for relevant gas turbine parameters (consult the app code for specific input features).
   - Enter your desired values in the input fields.
   - Submit the form.

3. **Output:**
   - The app will display the predicted values for NOx and CO emissions based on the trained models.
   - For both pollutants, it will also indicate whether the predicted values are considered anomalies based on the anomaly detection models.

**Customization and Further Development**

This repository provides a starting point for gas turbine anomaly prediction. You can customize the application by:

* Modifying `app.py` to tailor the web interface and input features.
* Updating `requirements.txt` with additional libraries if needed for advanced functionalities.
* Exploring the code for the pre-trained models to understand their training data and potentially retrain them with your own data for improved performance.

**Disclaimer**

The provided models are for educational and demonstration purposes only. Their accuracy depends on the specific training data used. For real-world applications, thorough testing and validation with high-quality data are crucial.

**Contributing**

Feel free to fork the repository and submit pull requests with improvements or bug fixes.
