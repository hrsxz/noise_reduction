# Signal Denoising with LSTM

## **Project Description**

### **Workflow**

#### **1. Data Generation**

- **Noisy Signal**: A sine wave signal with added random noise to simulate a noisy signal.
- **Clean Signal**: The target signal, which is a pure sine wave without noise.

#### **2. Data Preparation**

- Split the signal into multiple batches (`batches`) with a fixed sequence length (`sequence_length`).
- Use `DataLoader` to create a dataset for training the model.

#### **3. Model Design**

- A **LSTM network** is designed to process the noisy signal and learn to reconstruct the clean signal.  
- LSTM is chosen for its ability to capture temporal dependencies in sequential data.

#### **4. Model Training**

- **Loss Function**: Mean Squared Error (MSE) is used to minimize the difference between the predicted and clean signals.  
- The training process tracks the average loss per epoch to observe how well the model learns to denoise.

#### **5. Signal Denoising**

- The trained LSTM model is tested on noisy signals to generate denoised signals.  
- Compare the predicted denoised signals with the original clean signals to evaluate performance.

---

### **Further steps could be done**

1. **Noise Simulation**: Use realistic noise patterns, such as interference signals with multiple frequencies, instead of random Gaussian noise.

2. **Model Extension**: Expand the model to handle multi-channel signals (e.g., signals from multiple sensors).

3. **Real-World Testing**: Use real-world noisy signal data to validate the model's effectiveness.

---

## 🔃 Convert jupyter notebook to a report format

---

Find all notebooks and exchange the format to html

    find * -type f -name "*.ipynb"
    find * -type f -name "*.ipynb" -exec jupyter nbconvert --to html --output-dir docs/reports {} \;

Report format could be pdf/html/markdown and save under `docs/reports`

    jupyter nbconvert --to html --output-dir ../docs/reports "target_notebook_name.ipynb"

### **Solving the `application/vnd.plotly.v1+json` Rendering Issue**

#### **Problem Description**

When using `nbconvert` to convert a Jupyter Notebook to an HTML file, the following warning may appear:

   ```plaintext
   UserWarning: Your element with mimetype(s) dict_keys(['application/vnd.plotly.v1+json']) is not able to be represented.
   ```

This indicates that dynamic Plotly charts in the notebook are not being rendered correctly. The issue arises because the default Jupyter environment or template does not support rendering MIME type `application/vnd.plotly.v1+json`.

---

#### **Solution**

Install and enable the **Jupyter Notebook Renderers** extension, which supports rendering Plotly and other dynamic chart types.

- [Jupyter Notebook Renderers - VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter-renderers)


## Code2flow

[reference](https://github.com/scottrogowski/code2flow)

**pip install --upgrade notebook**

---