"""架构生成器"""
from typing import Dict, List


class SystemArchitect:
    """生成系统架构"""
    
    def __init__(self):
        self.components = {
            "user_management": {"name": "用户服务", "type": "service"},
            "api": {"name": "API 网关", "type": "gateway"},
            "database": {"name": "数据库", "type": "storage"},
            "cache": {"name": "缓存", "type": "cache"},
            "message_queue": {"name": "消息队列", "type": "mq"},
            "file_storage": {"name": "文件存储", "type": "storage"},
            "auth": {"name": "认证服务", "type": "service"},
            "payment": {"name": "支付服务", "type": "service"},
        }
    
    def design(self, components: List[str]) -> Dict:
        """设计架构"""
        nodes = []
        edges = []
        
        for comp in components:
            if comp in self.components:
                nodes.append({
                    "id": comp,
                    "name": self.components[comp]["name"],
                    "type": self.components[comp]["type"],
                })
        
        # 添加默认连接
        if "api" in components and "database" in components:
            edges.append({"from": "api", "to": "database"})
        if "api" in components and "cache" in components:
            edges.append({"from": "api", "to": "cache"})
        
        return {"nodes": nodes, "edges": edges}
