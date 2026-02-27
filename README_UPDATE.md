# Template Repository Upkeep

Yes, absolutely! 这个就是 Template Repo 最大的优势所在。即使你用 Template 新建了私库，你依然可以随时同步上游（Upstream）开源库的更新。

为了能够在你的私有 Repo 里随时拉取你这个开源版的最新 Agent 逻辑更新，你可以按照以下标准的 Git 工作流操作：

### 1. 配置上游仓库 (Upstream Remote)
在你的私有业务 Repo 目录下，添加这个开源 Repo 作为上游远程仓库：
```bash
git remote add upstream https://github.com/jameshou-ux/dsagents.git
```

你可以通过 `git remote -v` 检查是否配置成功。你应该能看到 `origin` (你的私有库) 和 `upstream` (这个开源库)。

### 2. 获取上游更新
当开源版的 AI Agent (比如 `ds-refactor-agent` 的 Prompt 优化了，或者 `run_pipeline.py` 更新了功能) 有了提交并推送到 GitHub 后，你可以：
```bash
# 获取开源库的所有最新变更，但不会自动合并到你的代码中
git fetch upstream
```

### 3. 合并更新到你的私有业务中
确保你在你私有库的主分支上（例如 `main`）：
```bash
# 将开源的最新核心代码合并到你的本地
git merge upstream/main
```

### 最佳实践建议：
因为你的私库会产出大量的定制化 `.json` (比如私有成分的 Design Tokens) 和 `.html` 报告，**请确保你的私有业务仓库保留并完善 `.gitignore`**，例如忽略 `0_gap-report/`、`1_audit-report/` 等生成目录。

只要你**不修改私库里引擎骨架的核心代码** (例如 `run_pipeline.py` 或 `.agent/skills/`)，你从 `upstream` 合并代码时就几乎**永远不会产生冲突**。

即使有冲突（比如你给私库里的 Prompt 加了点特效，开源版也改了 Prompt），Git 也会提示你手动解决冲突。这就像 Fork 一样，但由于它是以 Template 的形式创建的，你的每一次 Git 历史不需要被强行和开源板绑定在一起。
