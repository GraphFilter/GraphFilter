import os

from source.domain import Parameters
from source.domain.entities import BooleanStructuralInvariants
from source.domain.filter import Filter
from source.worker.export_pdf_worker import ExportPDFWorker

if __name__ == "__main__":
    current_path = os.getcwd()

    params = Parameters(
        location=current_path,
        name='example_report',
        method=Filter(),
        equation='x^2 + y^2 = z^2',
        conditions={
            BooleanStructuralInvariants.Planar(): True,
            BooleanStructuralInvariants.Biconnected(): False,
            BooleanStructuralInvariants.Bipartite(): True
        },
        description='This is a detailed description of the graph filtering process.',
        files=['file1.graph', 'file2.graph', 'file3.graph']
    )

    num_filtered_graphs = 4283
    num_input_graphs = 7598

    pdf_worker = ExportPDFWorker(params, num_filtered_graphs, num_input_graphs)
    pdf_worker.create_document()
