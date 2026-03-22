"""需求分析器"""
import re
from typing import Dict, List


class RequirementAnalyzer:
    """分析需求描述"""
    
    def __init__(self):
        self.patterns = {
            "user_management": ["用户", "登录", "注册", "权限", "role", "permission"],
            "api": ["API", "接口", "REST", "endpoint"],
            "database": ["数据库", "存储", "DB", "data"],
            "cache": ["缓存", "cache", "Redis"],
            "message_queue": ["队列", "消息", "MQ", "Kafka"],
            "file_storage": ["文件", "上传", "存储", "OSS", "S3"],
            "auth": ["认证", "授权", "JWT", "OAuth"],
            "payment": ["支付", "订单", "payment"],
        }
    
    def analyze(self, requirement: str) -> Dict:
        """分析需求"""
        requirement_lower = requirement.lower()
        
        components = []
        for comp, keywords in self.patterns.items():
            for kw in keywords:
                if kw.lower() in requirement_lower:
                    components.append(comp)
                    break
        
        return {
            "components": list(set(components)),
            "complexity": self._estimate_complexity(components),
            "suggestions": self._generate_suggestions(components),
        }
    
    def _estimate_complexity(self, components: List) -> str:
        if len(components) <= 2:
            return "low"
        elif len(components) <= 4:
            return "medium"
        return "high"
    
    def _generate_suggestions(self, components: List) -> List[str]:
        suggestions = []
        if "database" not in components:
            suggestions.append("建议添加数据库设计")
        if "cache" not in components:
            suggestions.append("考虑添加缓存层")
        return suggestions
