# README.md

🔃 Convert jupyter notebook to a report format

------------
Find all notebooks and exchange the format to html

    find * -type f -name "*.ipynb"
    find * -type f -name "*.ipynb" -exec jupyter nbconvert --to html --output-dir docs/reports {} \;

Report format could be pdf/html/markdown and save under `docs/reports`

    jupyter nbconvert --to html --output-dir ../docs/reports "target_notebook_name.ipynb"

**pip install --upgrade notebook**

---

### **功能描述**
1. **数据生成**
   - 模拟了一个带噪信号 `noisy_signal` 和一个对应的干净信号 `clean_signal`。
   - 干净信号是一个正弦波，带噪信号是在正弦波基础上添加了随机噪声。

2. **数据准备**
   - 将信号切分为多个批次 (`batches`)，每个批次包含一定数量的时间步长（`sequence_length`）。
   - 使用 `DataLoader` 创建数据集，用于后续的模型训练。

3. **模型设计**
   - 设计了一个 LSTM 网络，输入是带噪信号，目标是学习去噪，将输入的噪声信号还原为干净信号。
   - LSTM 是一种适合处理时序数据的网络结构，能够捕获时间序列中的相关性。

4. **模型训练**
   - 使用均方误差（MSE）作为损失函数，优化模型使输出的信号尽可能接近干净信号。
   - 训练过程中记录了每个 epoch 的平均损失，并观察模型逐渐学习还原信号的能力。

5. **信号降噪测试**
   - 使用训练好的模型对带噪信号进行预测。
   - 将预测的降噪信号与真实的干净信号对比，验证模型的性能。

---

### **降噪过程的具体实现**

#### **1. 输入信号**
带噪信号 `noisy_signal`：
- 随机生成的噪声添加到正弦波上，形状为 `(40000, 1)`，即 40000 个时间步，每个时间步的信号为 1 个值。

干净信号 `clean_signal`：
- 一个正弦波信号，表示目标信号，形状也为 `(40000, 1)`。

#### **2. 模型训练**
- 模型学习输入与目标信号之间的映射关系。
- LSTM 通过时间步之间的依赖关系，尝试捕获信号的原始形态，消除噪声。

#### **3. 模型预测**
- 输入带噪信号，输出降噪后的信号。
- 输出的信号形状与输入一致，为 `(batch_size, sequence_length, input_size)`。

#### **4. 可视化验证**
- 绘制降噪信号与目标干净信号的对比图，直观验证模型的性能。

---

### **代码的目标**

通过模拟的噪声数据，训练一个 LSTM 模型，完成 **带噪信号到干净信号的映射**，实现信号的降噪功能。

---

### **改进建议**
1. **噪声模型**
   - 当前的噪声是随机高斯噪声，可以考虑模拟更接近实际场景的噪声（如叠加多种频率成分的干扰信号）。

2. **模型评价**
   - 在训练后加入误差评价指标（如均方误差 MSE），量化降噪性能。
   ```python
   mse = torch.mean((denoised_signal - clean_signal) ** 2).item()
   print(f"Mean Squared Error: {mse:.4f}")
   ```

3. **模型扩展**
   - 当前模型仅处理单通道信号，可扩展到多通道信号（如同时处理多个传感器的时序数据）。

4. **数据扩展**
   - 可使用真实的带噪信号数据进行测试，以验证模型的实际效果。

---

### **总结**
你的代码的确实现了 **通过噪声信号还原干净信号** 的功能。模型训练了一个简单的 LSTM 降噪器，通过观察降噪信号与目标信号的对比，可以验证模型的有效性。

这是一个信号处理任务中常见的降噪应用，适用于音频、振动信号或其他时序数据的降噪任务。