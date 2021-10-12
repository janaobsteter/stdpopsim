#!/usr/bin/env python
# coding: utf-8

import msprime


demography = msprime.Demography()


# First, define all the parameters - the time of the split of the lineages
# and the subspecies and the effective populations at the splits.


# Parameters from the paper
# Ancestral size, before the split of the lineages
Na = 3.48e05  # TODO: THIS IS STILL A MEAN
##################################
# --- First split: lineages
##################################
# Time of split of the lineages
Ty_lineageSplit = 3e05
# Generation time
generation_time = 2  # TODO: Discuss this value!!!
# Time of split of the lineages in generations
Tg_lineageSplit = Ty_lineageSplit / generation_time

# Size of the populations after the split
N_A = 500184
N_M = 210043
# N_CO =

# Further split into C and O
Ty_COSplit = 1.65e05
Tg_COSplit = Ty_COSplit / generation_time
N_C = 189552
N_O = 298263

# We assume a constant population size from the split of the
# lineages to the split of subspecies
##################################
# --- Second split: subspecies
##################################
# Time of the split of the subspecies in years
Ty_A1Split = 32709
Ty_A2Split = 23187
Ty_M1Split = 37845
Ty_M2Split = 13069
Ty_CSplit = 24633
Ty_OSplit = 80646

# Time of the split of the subspecies in generations
Tg_A1Split = Ty_A1Split / generation_time
Tg_A2Split = Ty_A2Split / generation_time
Tg_M1Split = Ty_M1Split / generation_time
Tg_M2Split = Ty_M2Split / generation_time
Tg_CSplit = Ty_CSplit / generation_time
Tg_OSplit = Ty_OSplit / generation_time

# Sizes of the subspecie populations after the split
N_A_scutellata = 400005
N_A_capensis = 418821
N_A_adansonii = 457253
N_M_melliferaN = 157598
N_M_melliferaS = 177484
N_M_iberiensis = 217881
N_C_carnica = 168783
N_C_ligustica = 174353
N_O_syriaca = 313262
N_O_anatoliaca = 191419


# Next, let's create all the populations. We need an ancestral population before
# the split of the four lineages, one population for each of the
# (mitochondrial) lineages,
# and 10 populations for the subspecies. We also two need intermediate populations
# for the inner split of the A and the M subspecies.


# Add the ancestral population
demography.add_population(name="Ancestral", initial_size=Na)
# Add the four lineages
demography.add_population(name="A_lineage", initial_size=N_A)
demography.add_population(name="M_lineage", initial_size=N_M)
demography.add_population(name="C_lineage", initial_size=N_C)
demography.add_population(name="O_lineage", initial_size=N_O)
# Add the two populations for the internal splits in A and M lineage
demography.add_population(name="A_intermediate", initial_size=N_A)
demography.add_population(name="M_intermediate", initial_size=N_M)
# Add the ten subspecies
demography.add_population(name="A_adansonii", initial_size=N_A_adansonii)
demography.add_population(name="A_capensis", initial_size=N_A_capensis)
demography.add_population(name="A_scutellata", initial_size=N_A_scutellata)
demography.add_population(name="M_iberiensis", initial_size=N_M_iberiensis)
demography.add_population(name="M_melliferaN", initial_size=N_M_melliferaN)
demography.add_population(name="M_melliferaS", initial_size=N_M_melliferaS)
demography.add_population(name="C_carnica", initial_size=N_C_carnica)
demography.add_population(name="C_ligustica", initial_size=N_C_ligustica)
demography.add_population(name="O_syriaca", initial_size=N_O_syriaca)
demography.add_population(name="O_anatoliaca", initial_size=N_O_anatoliaca)


# Add the ancestral population
demography.add_population(
    name="Ancestral", initial_size=Na, extra_metadata={id: "Ancestral"}
)


# Let's check the demography.
demography.debug()


# Now let's add the splits, going from the present to the past: start with
# the split of the subspecies, followed by the split of the lineages.
# Now work from the bottom up
# First the split of the sublineages
# A lineage
# IT DOES NOT WORK WITHOUT THE INTERMEDIATE STEP
demography.add_population_split(
    time=Tg_A2Split, derived=["A_capensis", "A_scutellata"], ancestral="A_intermediate"
)
demography.add_population_split(
    time=Tg_A1Split, derived=["A_intermediate", "A_adansonii"], ancestral="A_lineage"
)


# demography.debug()

# M lineage
demography.add_population_split(
    time=Tg_M2Split,
    derived=["M_melliferaN", "M_melliferaS"],
    ancestral="M_intermediate",
)
demography.add_population_split(
    time=Tg_M1Split, derived=["M_intermediate", "M_iberiensis"], ancestral="M_lineage"
)

# C lineage
demography.add_population_split(
    time=Tg_CSplit, derived=["C_carnica", "C_ligustica"], ancestral="C_lineage"
)


# O lineage
demography.add_population_split(
    time=Tg_OSplit, derived=["O_syriaca", "O_anatoliaca"], ancestral="O_lineage"
)

# Merge the four lineages into the ancestral population
demography.add_population_split(
    time=Tg_lineageSplit,
    derived=["A_lineage", "M_lineage", "C_lineage", "O_lineage"],
    ancestral="Ancestral",
)


# Sort the demographic events.
demography.sort_events()


# Check the demography.
demography.debug()


# Simulate 10 samples of Apis mellifera carnica and 10 samples of
# Apis mellifera mellifera from the South.
# ts = msprime.sim_ancestry(samples={"C_carnica": 10, "M_melliferaS": 10},
# 		    demography=demography, random_seed=12)
# ts


# demography.populations
# demography.populations[0]
