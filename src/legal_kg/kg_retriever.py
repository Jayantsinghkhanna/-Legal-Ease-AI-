class LegalKGRetriever:

    def __init__(
        self,
        graph
    ):
        self.graph = graph

    def get_neighbors(
        self,
        entity
    ):

        if entity not in self.graph:
            return []

        neighbors = []

        for node in self.graph.neighbors(
            entity
        ):
            neighbors.append(
                node
            )

        return neighbors

    def retrieve_context(
        self,
        entity
    ):

        if entity not in self.graph:
            return []

        facts = []

        for neighbor in self.graph.neighbors(
            entity
        ):

            edge_data = (
                self.graph.get_edge_data(
                    entity,
                    neighbor
                )
            )

            relation = edge_data.get(
                "relation",
                "related_to"
            )

            facts.append(
                f"{entity} --{relation}--> {neighbor}"
            )

        return facts