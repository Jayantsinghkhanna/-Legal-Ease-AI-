import networkx as nx


class LegalKGBuilder:

    def __init__(self):

        self.graph = nx.MultiDiGraph()

    def add_knowledge(
        self,
        knowledge
    ):

        for fact in knowledge.facts:

            self.graph.add_node(
                fact.party,
                type="party"
            )

            self.graph.add_node(
                fact.obligation,
                type="obligation"
            )

            self.graph.add_node(
                fact.clause_type,
                type="clause"
            )

            self.graph.add_edge(
                fact.party,
                fact.obligation,
                relation="must"
            )

            self.graph.add_edge(
                fact.obligation,
                fact.clause_type,
                relation="belongs_to"
            )

            if fact.deadline:

                self.graph.add_node(
                    fact.deadline,
                    type="deadline"
                )

                self.graph.add_edge(
                    fact.obligation,
                    fact.deadline,
                    relation="deadline"
                )

        return self.graph