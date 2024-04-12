import copy

te0803_boards = ["2cg", "2eg", "3cg", "3eg", "4cg", "4eg", "4ev", "5ev"]
te0808_boards = ["6eg", "9eg", "15eg"]

te0803_som_revisions = { "2cg" : [1.0],
                         "2eg" : [1.0],
                         "3cg" : [1.0, 5.0],
                         "3eg" : [1.0, 3.0, 5.0],
                         "4cg" : [1.0],
                         "4eg" : [1.0, 3.0],
                         "4ev" : [1.0, 3.0],
                         "5ev" : [1.0],
                       }

te0803_som_revisions_tebf = { "2cg" : [2.0],
                              "2eg" : [2.0],
                              "3cg" : [2.0, 6.0],
                              "3eg" : [2.0, 4.0, 6.0],
                              "4cg" : [2.0],
                              "4eg" : [2.0, 4.0],
                              "4ev" : [2.0, 4.0],
                              "5ev" : [2.0],
                            }

te0808_som_revisions = { "6eg"  : [3.0],
                         "9eg"  : [1.0, 3.0],
                         "15eg" : [3.0],
                       }

te0808_som_revisions_tebf = { "6eg"  : [4.0],
                              "9eg"  : [2.0, 4.0],
                              "15eg" : [4.0],
                            }

te080x_boards = copy.deepcopy(te0803_boards)
te080x_boards.extend(te0808_boards)

te080x_som_revisions = copy.deepcopy(te0803_som_revisions)
te080x_som_revisions.update(te0808_som_revisions)

te080x_som_revisions_tebf = copy.deepcopy(te0803_som_revisions_tebf)
te080x_som_revisions_tebf.update(te0808_som_revisions_tebf)
