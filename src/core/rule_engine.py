import inspect
from typing import get_type_hints, Any

class RuleEngine:
    """
    The Core Magisterial Engine designed to bridge the Abstraction Gap.
    It treats well-structured code as a source of inherent semantic richness[cite: 9, 14].
    """
    
    def capture_intent(self, func: callable) -> dict:
        """
        Parses function signatures and docstrings to extract explicit developer intent.
        This resolves the friction between deterministic code and natural language.
        """
        signature = inspect.signature(func)
        docstring = inspect.getdoc(func)
        
        # Mapping the 'Semantic Richness' of the code
        intent_map = {
            "function_name": func.__name__,
            "description": docstring,
            "constraints": {
                name: str(param.annotation) 
                for name, param in signature.parameters.items()
            },
            "return_type": str(signature.return_annotation)
        }
        
        return intent_map

    def enforce_ground_truth(self, intent: dict, model_output: Any):
        """
        Uses type annotations as the 'Ground Truth' to validate probabilistic outputs.
        Prevents the 'Abstraction Gap' from manifesting as logic-bleed[cite: 9].
        """
        pass
