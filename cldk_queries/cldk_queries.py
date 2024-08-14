from pathlib import Path
from typing import List, Dict

from cldk import CLDK
from cldk.models.java import JCallable
from cldk.models.java.models import JField

import constants


class CLDKQueries:
    def __init__(self, project_root: str, is_analysis_needed: bool = False):
        self.dataset_path = Path(project_root).parent
        self.project_root = project_root
        self.dataset = Path(project_root).name
        self.test_root = str(Path("src/test/java"))
        project_dir = Path.cwd().joinpath(self.dataset_path, self.dataset).__str__()
        cldk = CLDK(language="java")
        self.analysis = cldk.analysis(
            project_path=project_dir,
            analysis_level="call-graph",
            analysis_backend="codeanalyzer",
            analysis_json_path=Path.cwd().joinpath(constants.EVALUATE_OUTPUT_DIR, self.dataset),
            eager=is_analysis_needed
        )

    def get_src_classes(self) -> List[str]:
        """
        Get source classes
        Returns:

        """
        src_classes = []
        all_classes = self.analysis.get_classes()
        for class_name in all_classes:
            source_file_path = self.analysis.get_java_file(class_name)
            if self.test_root in source_file_path:
                src_classes.append(class_name)
        return src_classes

    def get_constructors(self) -> dict[str, JCallable]:
        """
        Get all constructors
        Returns:
            dict[str, JCallable]: all constructors defined in each class
        """
        constructors = {}
        all_classes = self.analysis.get_classes()
        for class_name in all_classes:
            source_file_path = self.preprocessor.ns_preprocessor.get_java_file(class_name)
            if self.test_root in source_file_path:
                constructors[class_name] = self.analysis.get_constructors(qualified_class_name=class_name)
        return constructors

    def get_methods(self, qualified_class_name: str) -> Dict[str, Dict[str, JCallable]]:
        """
        Returns a dictionary of all methods in the Java code with
          qualified class name as key and dictionary of methods in that class
          as value

        Returns:
        --------
        Dict[str, Dict[str, JCallable]]:
            A dictionary of dictionaries of all methods in the Java code.
        """
        return self.analysis.get_methods(qualified_class_name=qualified_class_name)

    def get_fields(self, qualified_class_name: str) -> List[JField]:
        """
        Returns a list of fields given a qualified class name
        Args:
            qualified_class_name:

        Returns:

        """
        return self.analysis.get_fields(qualified_class_name=qualified_class_name)

    def get_imports(self, qualified_class_name: str) -> List[str]:
        """
        Returns a list of imports given a qualified class name
        Args:
            qualified_class_name: qualified class name

        Returns:

        """
        file_path = self.analysis.get_java_file(qualified_class_name=qualified_class_name)
        if not file_path:
            return []
        java_compilation_unit = self.analysis.get_java_compilation_unit(file_path=file_path)
        return ['import ' + imports + ';' for imports in java_compilation_unit.imports]

    def get_nested_classes(self, qualified_class_name: str) -> None:
        pass

    def get_super_classes(self, qualified_class_name: str) -> List[str]:
        """
        Returns a list of super classes given a qualified class name
        Args:
            qualified_class_name:

        Returns:

        """
        return self.analysis.get_class(qualified_class_name=qualified_class_name).extends_list
