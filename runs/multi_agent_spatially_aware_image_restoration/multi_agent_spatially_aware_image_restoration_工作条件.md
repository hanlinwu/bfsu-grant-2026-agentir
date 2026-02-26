# 工作条件 - Multi-Agent Collaborative Spatially-Aware Image Restoration

## Meta
- **主题**: Multi-Agent Collaborative Spatially-Aware Image Restoration
- **档位**: Premium（旗舰级）
- **目标字数**: 10,000–15,000 words
- **目标参考文献数**: 80–150 篇
- **最高原则**: AI 不得为赶进度偷懒或短视，必须以最佳可用证据与写作质量完成综述
- **日期**: 2026-02-26

## Search Plan & Search Log

### 检索策略
- 多查询检索，共 25 组查询变体（15 组初始 + 10 组补充）
- 数据源：OpenAlex API（零配置主力源）
- 时间范围：以 2023–2025 为主，重要经典文献追溯至更早

### 查询变体
**第一轮（15组）：**
1. agent image restoration LLM tool planning
2. multi-agent visual task planning large language model
3. all-in-one image restoration unified model degradation
4. prompt-based image restoration learning degradation
5. image restoration transformer architecture efficient
6. image denoising deblurring dehazing deraining deep learning
7. segment anything model SAM zero-shot segmentation
8. visual language model image quality assessment
9. image quality assessment no-reference blind deep learning
10. knowledge distillation model compression image restoration
11. spatially varying degradation image restoration local
12. diffusion model image restoration generation
13. large multimodal model tool use visual reasoning
14. image super resolution continuous scale arbitrary
15. real world image degradation mixed complex restoration

**第二轮补充（10组）：**
1. AgenticIR agentic image restoration
2. RestoreAgent autonomous image restoration multimodal
3. MAIR multi-agent image restoration degradation prior
4. Q-Agent quality-driven agent image restoration greedy
5. AirNet all-in-one image restoration contrastive learning
6. InstructIR instruction-based image restoration natural language
7. SwinIR image restoration Swin Transformer
8. DepictQA depicted image quality assessment language
9. IPR-LLM image processing LLM reasoning chain
10. visual agent tool use image editing generation

### 检索结果
- 第一轮初检文献：651 条
- 第二轮补充文献：166 条
- 去重后合计：788 条唯一论文

## Dedup
- 去重策略：标题规范化 + DOI 优先 + 模糊匹配（SequenceMatcher + token Jaccard）
- 去重阈值：title_similarity=0.92, token_jaccard=0.80
- 第一轮：651 → 650（合并 1 对）
- 合并后总计（含补充）：788 条唯一论文

## Relevance Scoring & Selection

### 评分方法
- AI 逐篇阅读标题和摘要，按 1-10 分评分
- 评分标准：
  - 9-10: 完美匹配 - 相同任务 + 相同方法 + 相同模态
  - 7-8: 高度相关 - 相同任务，方法/模态略有差异
  - 5-6: 中等相关 - 同领域但任务/方法有显著差异
  - 3-4: 弱相关 - 仅部分概念重叠
  - 1-2: 几乎无关

### 评分分布
| 分数段 | 数量 | 百分比 |
|--------|------|--------|
| 9-10 | 23 | 2.9% |
| 7-8 | 95 | 12.1% |
| 5-6 | 99 | 12.6% |
| 3-4 | 80 | 10.2% |
| 1-2 | 491 | 62.3% |
| **总计** | **788** | **100%** |

### 选文策略
- 高分优先：所有 score ≥ 7 的论文优先选入
- 目标参考文献数：~115（midpoint of 80-150）
- 补充手动添加 5 篇关键论文（AgenticIR, Q-Agent, AirNet, InstructIR, DepictQA）
- **最终选文：123 篇**

### 子主题分布
| 子主题 | 数量 |
|--------|------|
| All-in-One Restoration | 40 |
| Diffusion Restoration | 24 |
| Transformer Restoration | 23 |
| Image Quality Assessment | 12 |
| Real-World Degradation | 9 |
| Agent-Based Restoration | 6 |
| Knowledge Distillation | 5 |
| Foundation Models Vision | 4 |

## Review Structure

### 综述结构（11 sections）
1. **Abstract** (~220 words) - 单段式摘要
2. **Introduction** (~770 words) - 问题定义→发展脉络→研究空白→本综述目标
3. **Transformer-Based Single-Task Restoration** (~1200 words) - 6 subsections
4. **All-in-One Unified Restoration** (~1600 words) - 7 subsections
5. **Diffusion-Based Generative Restoration** (~1100 words) - 5 subsections
6. **Agent-Based Restoration Systems** (~900 words) - 4 subsections
7. **Foundation Models for Analysis and IQA** (~800 words) - 4 subsections
8. **Model Compression and Lightweight Deployment** (~500 words) - 2 subsections
9. **Discussion** (~500 words) - 3 subsections
10. **Perspectives and Future Directions** (~400 words) - 4 subsections
11. **Conclusion** (~230 words)

## Validation
- 正文字数：~10,236 words ✅ (Premium: 10,000-15,000)
- 参考文献数：123 篇 ✅ (Premium: 80-150)
- 必需章节：Abstract ✅, Introduction ✅, Discussion ✅, Conclusion ✅
- \cite 与 BibTeX key 一致性：123/123 匹配，0 缺失，0 未使用 ✅
- PDF 编译：成功 ✅ (35 pages)
- Word 导出：成功 ✅
