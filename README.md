# 自然語言處理期中專案

本專案為淡江大學人工智慧學系「自然語言處理」課程的期中專題，內容涵蓋新聞爬蟲、關鍵字抽取、文字分類等。

## 執行說明

### 最建議的執行方式：Google Colab

本專案所有 Jupyter Notebook 已在 [Google Colab](https://colab.research.google.com/) 測試通過。  
建議直接將 `.ipynb` 檔案上傳到 Colab 執行，無需擔心環境安裝問題。

### 在本地端（VSCode/Jupyter）執行

若要在本地端執行，請注意需要安裝以下 Python 套件：
- requests
- beautifulsoup4
- pandas
- matplotlib
- transformers
- torch
- 以及其它程式中有用到的套件

可以用以下指令安裝（如果有 requirements.txt）：
pip install -r requirements.txt

若本地執行出現環境或套件問題，建議優先使用 Colab 執行。

### 常見問題

- Colab 有預裝大多數資料科學與 NLP 套件，VSCode 需手動安裝套件。
- 若本地端遇到「找不到套件」、「GPU 設定錯誤」等問題，可先切換到 CPU 執行，或直接於 Colab 測試。

---

## 專案內容

- UDN 新聞爬蟲（Python）
- 中文關鍵字抽取（Python/Julia）
- GPT-2 文本分類（Jupyter Notebook）

## 專案結構
Midterm-Project-NLP/
├── gpt2.ipynb
├── keyword.jl
├── README.md
├── 爬蟲/
│ ├── 412777095_新聞_期中.ipynb
│ ├── udn.py
│ ├── udn_key-3.py
│ ├── keyword1.jl
│ ├── keyword2.jl
│ └── others.jl
└── ...
