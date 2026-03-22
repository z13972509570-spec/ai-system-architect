"""图表生成器"""
from typing import Dict


class DiagramGenerator:
    """生成架构图"""
    
    def to_mermaid(self, architecture: Dict) -> str:
        """生成 Mermaid 图表"""
        lines = ["```mermaid", "flowchart TB"]
        
        # 添加节点
        for node in architecture.get("nodes", []):
            shape = self._get_shape(node["type"])
            lines.append(f"    {node['id']}{shape}{{{node['name']}}}")
        
        # 添加连接
        for edge in architecture.get("edges", []):
            lines.append(f"    {edge['from']} --> {edge['to']}")
        
        lines.append("```")
        return "\n".join(lines)
    
    def to_plantuml(self, architecture: Dict) -> str:
        """生成 PlantUML"""
        lines = ["@startuml"]
        
        for node in architecture.get("nodes", []):
            if node["type"] == "service":
                lines.append(f"package {node['name']} {{")
                lines.append("    [service]")
                lines.append("}")
            elif node["type"] == "storage":
                lines.append(f"database {node['name']}")
            elif node["type"] == "gateway":
                lines.append(f"frame {node['name']}")
        
        for edge in architecture.get("edges", []):
            lines.append(f"{edge['from']} --> {edge['to']}")
        
        lines.append("@enduml")
        return "\n".join(lines)
    
    def _get_shape(self, node_type: str) -> str:
        shapes = {
            "service": "([",
            "gateway": "([",
            "storage": "[(",
            "cache": "[(",
            "mq": "((",
        }
        closings = {
            "service": "])",
            "gateway": "])",
            "storage": "))",
            "cache": "))",
            "mq": "))",
        }
        return shapes.get(node_type, "["), closings.get(node_type, "]")
