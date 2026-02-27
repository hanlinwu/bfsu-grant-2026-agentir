# Thread 4 质量检查报告：缩略语规范、术语一致性、图表引用

**检查日期**: 2026-02-27
**检查范围**: main.tex 及 sections/ 目录下所有章节文件
**检查人员**: Claude Code (QC Agent)

---

## 1. Thread 执行摘要

本次质量检查聚焦于 NSFC 标书的**缩略语规范**、**术语一致性**和**图表引用完整性**三个维度。通过对主文件及 10 个章节文件的系统性审查，共发现 **3 个 P1 级问题**（需修正）、**5 个 P2 级问题**（建议改进），无 P0 级严重问题。

**总体评估**: 文档整体质量良好，缩略语使用基本规范，术语一致性较好，图表引用完整。但存在个别缩略语首次使用未展开、术语大小写不一致等问题需要修正。

---

## 2. 缩略语使用规范检查表

### 2.1 首次使用规范检查

| 缩略语 | 全称 | 首次出现位置 | 是否规范展开 | 状态 |
|--------|------|--------------|--------------|------|
| SAM | Segment Anything Model | sections/01-topic-basis.tex 第 74 行 | 是（"SAM（Segment Anything Model）"） | ✅ 规范 |
| VLM | Visual Language Model | sections/01-topic-basis.tex 第 62 行 | **否** | ⚠️ **P1** |
| LLM | Large Language Model | sections/01-topic-basis.tex 第 62 行 | **否** | ⚠️ **P1** |
| PSNR | Peak Signal-to-Noise Ratio | sections/01-topic-basis.tex 第 9 行 | **否** | ⚠️ **P1** |
| SSIM | Structural Similarity Index | sections/01-topic-basis.tex 第 56 行 | **否** | ⚠️ **P2** |
| LPIPS | Learned Perceptual Image Patch Similarity | sections/01-topic-basis.tex 第 9 行 | **否** | ⚠️ **P2** |
| AiO | All-in-One | sections/01-topic-basis.tex 第 7 行 | 是（"All-in-One（AiO）"） | ✅ 规范 |
| CNN | Convolutional Neural Network | sections/01-topic-basis.tex 第 40 行 | **否** | ⚠️ **P2** |
| AiO | All-in-One | sections/01-topic-basis.tex 第 44 行 | 重复展开 | ⚠️ **P2** |

### 2.2 详细问题描述

#### P1-1: VLM 首次使用未展开
- **位置**: sections/01-topic-basis.tex 第 62 行
- **问题描述**: "视觉语言模型（VLM）"首次出现时，直接使用了缩略语 VLM，未给出英文全称
- **当前文本**: "视觉语言模型（VLM）或大语言模型（LLM）作为协调决策者"
- **修改建议**: 改为"视觉语言模型（Visual Language Model, VLM）或大语言模型（Large Language Model, LLM）"

#### P1-2: LLM 首次使用未展开
- **位置**: sections/01-topic-basis.tex 第 62 行
- **问题描述**: 同上，LLM 首次使用未给出英文全称
- **修改建议**: 同上

#### P1-3: PSNR 首次使用未展开
- **位置**: sections/01-topic-basis.tex 第 9 行
- **问题描述**: "代表性模型的PSNR较单一退化场景下降1.5--3.0~dB"中 PSNR 首次出现未展开
- **当前文本**: "代表性模型的PSNR较单一退化场景下降"
- **修改建议**: 改为"代表性模型的峰值信噪比（Peak Signal-to-Noise Ratio, PSNR）较单一退化场景下降"

### 2.3 P2 级问题

#### P2-1: SSIM 首次使用未展开
- **位置**: sections/01-topic-basis.tex 第 56 行
- **问题描述**: "在感知质量评估指标（LPIPS、SSIM等）"中 SSIM 首次出现未展开
- **修改建议**: 改为"在感知质量评估指标（学习感知图像块相似度 LPIPS、结构相似性指数 SSIM 等）"

#### P2-2: LPIPS 首次使用未展开
- **位置**: sections/01-topic-basis.tex 第 9 行（与 PSNR 同时出现）
- **问题描述**: LPIPS 首次出现未给出英文全称
- **修改建议**: 在首次出现时改为"学习感知图像块相似度（Learned Perceptual Image Patch Similarity, LPIPS）"

#### P2-3: CNN 首次使用未展开
- **位置**: sections/01-topic-basis.tex 第 40 行
- **问题描述**: "结合CNN局部纹理提取能力"中 CNN 首次出现未展开
- **修改建议**: 改为"结合卷积神经网络（Convolutional Neural Network, CNN）局部纹理提取能力"

#### P2-4: AiO 重复展开
- **位置**: sections/01-topic-basis.tex 第 44 行
- **问题描述**: AiO 已在第 7 行展开为"All-in-One（AiO）"，第 44 行再次展开为"All-in-One（AiO）"
- **修改建议**: 第 44 行直接使用 AiO 即可，无需重复展开

---

## 3. 术语一致性检查结果

### 3.1 大小写一致性

| 术语 | 出现形式 | 位置 | 建议统一形式 |
|------|----------|------|--------------|
| All-in-One | "All-in-One" | sections/01-topic-basis.tex 第 7、44 行 | All-in-One（已统一）✅ |
| AiO | "AiO" | sections/01-topic-basis.tex 第 7、44、52 行 | AiO（已统一）✅ |
| multi-agent | "多智能体" | 全文 | 中文"多智能体"已统一 ✅ |
| 智能体化 | "智能体化" | sections/01-topic-basis.tex 第 7 行 | 已统一 ✅ |

### 3.2 连字符使用

| 术语 | 使用情况 | 状态 |
|------|----------|------|
| multi-agent | 未直接使用英文，使用"多智能体" | ✅ 规范 |
| All-in-One | 使用连字符形式 | ✅ 规范 |
| Chain-of-Thought | sections/01-topic-basis.tex 第 50 行 | ✅ 规范 |

### 3.3 中英文混用一致性

| 概念 | 中文表达 | 英文表达 | 状态 |
|------|----------|----------|------|
| 图像恢复 | Image Restoration | 统一使用"图像恢复" | ✅ |
| 空间退化图 | Spatial Degradation Map | 统一使用"空间退化图" | ✅ |
| 轨迹蒸馏 | Trajectory Distillation | 统一使用"轨迹蒸馏" | ✅ |
| 全局调度器 | Global Scheduler | 统一使用"全局调度器" | ✅ |
| 区域专家 | Regional Expert | 统一使用"区域专家" | ✅ |

### 3.4 发现的问题

#### P2-5: Transformer 与 transformer 大小写不一致
- **位置**:
  - "Transformer": sections/01-topic-basis.tex 第 34、36、42 行
  - "transformer": sections/01-topic-basis.tex 第 48 行（"Transformer主干"）
- **问题描述**: 作为架构名称应统一首字母大写
- **修改建议**: 统一使用 "Transformer"

---

## 4. 图表引用完整性检查

### 4.1 图表清单

| 图编号 | 标签 | 文件名 | 引用位置 | 状态 |
|--------|------|--------|----------|------|
| 图 1 | fig:framework-contrast | imgs/Gemini_Generated_Image_lk4hu6lk4hu6lk4h.png | sections/01-topic-basis.tex 第 23 行 | ✅ 已引用 |
| 图 2 | fig:overall-framework | imgs/Gemini_Generated_Image_lk4hu6lk4hu6lk4h.png | sections/02-goals-framework-challenges.tex 第 15 行 | ✅ 已引用 |
| 图 3 | fig:method-pipeline | imgs/Gemini_Generated_Image_qjhpc4qjhpc4qjhp.png | sections/03-methodology.tex 第 7 行 | ✅ 已引用 |

### 4.2 图表引用检查

#### 正向检查（正文引用 -> 图表存在性）

| 引用位置 | 引用内容 | 对应图表 | 状态 |
|----------|----------|----------|------|
| sections/01-topic-basis.tex 第 23 行 | 图~\ref{fig:framework-contrast} | fig:framework-contrast | ✅ 存在 |
| sections/02-goals-framework-challenges.tex 第 15 行 | 图~\ref{fig:overall-framework} | fig:overall-framework | ✅ 存在 |
| sections/03-methodology.tex 第 7 行 | 图~\ref{fig:method-pipeline} | fig:method-pipeline | ✅ 存在 |

#### 反向检查（图表 -> 正文引用）

所有 3 个图表均被正文正确引用，无孤立图表。

### 4.3 公式编号检查

| 公式位置 | 公式内容 | 是否有编号 | 状态 |
|----------|----------|------------|------|
| sections/03-methodology.tex 第 98 行 | SAM分割公式 | 有 (1) | ✅ |
| sections/03-methodology.tex 第 102 行 | 置信度门控公式 | 有 (2) | ✅ |
| sections/03-methodology.tex 第 108 行 | VLM退化分析公式 | 有 (3) | ✅ |
| sections/03-methodology.tex 第 112 行 | 上下文聚合公式 | 有 (4) | ✅ |
| sections/03-methodology.tex 第 118 行 | 空间退化图公式 | 有 (5) | ✅ |
| sections/03-methodology.tex 第 130 行 | 优先级函数公式 | 有 (6) | ✅ |
| sections/03-methodology.tex 第 134 行 | 全局策略向量公式 | 有 (7) | ✅ |
| sections/03-methodology.tex 第 140 行 | 区域修复公式 | 有 (8) | ✅ |
| sections/03-methodology.tex 第 145 行 | 策略梯度公式 | 有 (9) | ✅ |
| sections/03-methodology.tex 第 151 行 | 参数优化公式 | 有 (10) | ✅ |
| sections/03-methodology.tex 第 157 行 | 全局融合公式 | 有 (11) | ✅ |
| sections/03-methodology.tex 第 161 行 | 一致性损失公式 | 有 (12) | ✅ |
| sections/03-methodology.tex 第 171 行 | 轨迹数据集公式 | 有 (13) | ✅ |
| sections/03-methodology.tex 第 185 行 | 分割头公式 | 有 (14) | ✅ |
| sections/03-methodology.tex 第 190 行 | 分类头公式 | 有 (15) | ✅ |
| sections/03-methodology.tex 第 196 行 | 路由头公式 | 有 (16) | ✅ |
| sections/03-methodology.tex 第 202 行 | 参数头公式 | 有 (17) | ✅ |
| sections/03-methodology.tex 第 208 行 | 多任务损失公式 | 有 (18) | ✅ |
| sections/03-methodology.tex 第 221 行 | 知识蒸馏损失公式 | 有 (19) | ✅ |
| sections/03-methodology.tex 第 231 行 | 困难样本损失公式 | 有 (20) | ✅ |
| sections/03-methodology.tex 第 236 行 | 部署推理公式 | 有 (21) | ✅ |

**公式编号检查结论**: 所有重要公式均有编号，编号连续，无跳号或重复。

### 4.4 浮动位置检查

| 图表 | 浮动环境 | 位置参数 | 评估 |
|------|----------|----------|------|
| fig:framework-contrast | figure[H] | H（强制 here） | ✅ 合适，使用 float 包 |
| fig:overall-framework | figure[H] | H（强制 here） | ✅ 合适 |
| fig:method-pipeline | figure[H] | H（强制 here） | ✅ 合适 |

所有图表均使用 `[H]` 参数强制固定在指定位置，符合基金申请书对图表位置可控性的要求。

---

## 5. P0/P1/P2 问题清单

### 5.1 P0 级问题（严重，必须修正）

无 P0 级问题。

### 5.2 P1 级问题（重要，建议修正）

| 编号 | 问题 | 位置 | 修改建议 |
|------|------|------|----------|
| P1-1 | VLM 首次使用未展开 | sections/01-topic-basis.tex 第 62 行 | 改为"视觉语言模型（Visual Language Model, VLM）" |
| P1-2 | LLM 首次使用未展开 | sections/01-topic-basis.tex 第 62 行 | 改为"大语言模型（Large Language Model, LLM）" |
| P1-3 | PSNR 首次使用未展开 | sections/01-topic-basis.tex 第 9 行 | 改为"峰值信噪比（Peak Signal-to-Noise Ratio, PSNR）" |

### 5.3 P2 级问题（次要，可选修正）

| 编号 | 问题 | 位置 | 修改建议 |
|------|------|------|----------|
| P2-1 | SSIM 首次使用未展开 | sections/01-topic-basis.tex 第 56 行 | 补充英文全称 |
| P2-2 | LPIPS 首次使用未展开 | sections/01-topic-basis.tex 第 9 行 | 补充英文全称 |
| P2-3 | CNN 首次使用未展开 | sections/01-topic-basis.tex 第 40 行 | 补充英文全称 |
| P2-4 | AiO 重复展开 | sections/01-topic-basis.tex 第 44 行 | 直接使用 AiO，删除括号内展开 |
| P2-5 | Transformer 大小写不一致 | sections/01-topic-basis.tex 多处 | 统一使用首字母大写的 "Transformer" |

---

## 6. 附录：详细引用位置

### 6.1 缩略语出现位置详表

```
SAM:
  - sections/01-topic-basis.tex:74  "Kirillov等人\cite{sam}提出的SAM（Segment Anything Model）"
  - sections/01-topic-basis.tex:83  "利用零样本分割模型SAM\cite{sam}"
  - sections/02-goals-framework-challenges.tex:83  "利用零样本分割模型SAM\cite{sam}"
  - sections/03-methodology.tex:96  "利用零样本分割模型SAM\cite{sam}"

VLM:
  - sections/01-topic-basis.tex:62  "视觉语言模型（VLM）或大语言模型（LLM）" [首次使用，未展开]
  - sections/01-topic-basis.tex:76  "经Q-Instruct微调的视觉语言模型"
  - sections/03-methodology.tex:106  "将$\mathbf{y}_{R_i}$输入经Q-Instruct数据集微调的视觉语言模型"

LLM:
  - sections/01-topic-basis.tex:62  "视觉语言模型（VLM）或大语言模型（LLM）" [首次使用，未展开]
  - sections/01-topic-basis.tex:64  "RestoreAgent\cite{restoreagent}通过在大规模恢复任务...微调多模态LLM"

PSNR:
  - sections/01-topic-basis.tex:9  "代表性模型的PSNR较单一退化场景下降1.5--3.0~dB" [首次使用，未展开]
  - sections/01-topic-basis.tex:36  "提升0.14--0.31~dB PSNR"
  - sections/02-goals-framework-challenges.tex:267  "PSNR提升$\geq$0.5dB"
  - sections/03-methodology.tex:239  "PSNR损失$\leq$5\%"

SSIM:
  - sections/01-topic-basis.tex:56  "在感知质量评估指标（LPIPS、SSIM等）" [首次使用，未展开]
  - sections/03-methodology.tex:239  "SSIM损失$\leq$3\%"

LPIPS:
  - sections/01-topic-basis.tex:9  "LPIPS感知质量指标出现系统性退化" [首次使用，未展开]
  - sections/01-topic-basis.tex:56  "在感知质量评估指标（LPIPS、SSIM等）"

AiO:
  - sections/01-topic-basis.tex:7  "All-in-One统一模型\cite{airnet,promptir,instructir}" [首次使用]
  - sections/01-topic-basis.tex:44  "统一化All-in-One（AiO）图像恢复方法" [重复展开]
  - sections/01-topic-basis.tex:52  "Jiang等人\cite{aio_survey}在系统综述中明确指出AiO方法"

CNN:
  - sections/01-topic-basis.tex:40  "结合CNN局部纹理提取能力" [首次使用，未展开]
```

---

## 7. 总结与建议

### 7.1 总体评价

1. **缩略语规范**: 整体使用规范，但存在 3 个重要缩略语（VLM、LLM、PSNR）首次使用未展开的问题，建议优先修正。
2. **术语一致性**: 术语使用较为一致，大小写和连字符使用基本规范。
3. **图表引用**: 所有图表均有正确引用，公式编号完整连续，浮动位置设置恰当。

### 7.2 优先修正建议

**高优先级（P1）**:
1. 在 sections/01-topic-basis.tex 第 62 行补充 VLM 和 LLM 的英文全称
2. 在 sections/01-topic-basis.tex 第 9 行补充 PSNR 的中文名称和英文全称

**中优先级（P2）**:
1. 统一 Transformer 的大小写
2. 删除 AiO 的重复展开
3. 补充 SSIM、LPIPS、CNN 的英文全称（如空间允许）

---

*报告生成时间: 2026-02-27*
*检查工具: Claude Code QC Agent*
