import pandas as pd
import numpy as np
from typing import Union, List, Dict, Tuple

    
def build_toy_dataset(**kwargs):
    '''
    Builds a toy dataset with fixed records.
    
    Returns:
    - A tuple containing:
        * Dataset as a Pandas Dataframe
        * List of quasi-identifiers
        * Sensitive column name
    '''
    data = [
        [6, "1", "test1", "x", 20],
        [6, "1", "test1", "x", 30],
        [8, "2", "test2", "x", 50],
        [8, "2", "test3", "w", 45],
        [8, "1", "test2", "y", 35],
        [4, "2", "test3", "y", 20],
        [4, "1", "test3", "y", 20],
        [2, "1", "test3", "z", 22],
        [2, "2", "test3", "y", 32],
    ]

    columns = ["col1", "col2", "col3", "col4", "col5"]
    categorical = set(("col2", "col3", "col4"))

    df = pd.DataFrame(data=data, columns=columns)


    for name in categorical:
        df[name] = df[name].astype("category")

    return df, ["col1", "col2", "col3"], 'col4'

def generate_random_dataset(n: int=200, **kwargs):
    '''
    Generates a toy dataset containing n distinct samples.

    - n: number of samples to generate

    Returns:
    - A tuple containing:
        * Dataset as a Pandas Dataframe
        * List of quasi-identifiers
        * Sensitive column name
    '''
    diseases = np.array(["Angine", "Appendicite", "Chlamydia", "Cataracte", "Dengue", 
                         "Eczéma", "Grippe", "Hépatite B", "Hépatite C", "Rhino-pharyngite", 
                         "Otite", "Rougeole", "Scarlatine", "Urticaire", "Varicelle", "Zona"])
    zipcodes = np.array([35000, 35200, 37000, 40000, 40500, 50000, 52000, 60000, 62000, 68000, 
                         75000, 75001, 75002, 75005])

    rows = []
    for _ in range(n):
        row = {'Age':np.random.randint(7, 77), 'ZipCode':np.random.choice(zipcodes), 'Disease':np.random.choice(diseases)}
        while row in rows:
            row = {'Age':np.random.randint(7, 77), 'ZipCode':np.random.choice(zipcodes), 'Disease':np.random.choice(diseases)}
        rows.append(row)
        
        
    dataset = pd.DataFrame(rows)
    dataset.sort_values(by = ['Age', 'ZipCode'], inplace=True)

    return dataset, ['Age', 'ZipCode'], 'Disease'

def read_adult(path: str, **kwargs) -> pd.DataFrame:
    '''
    Reads the adult dataset.

    Parameters:
        - path: path to the CSV file
    
    Returns:
    - A tuple containing:
        * Dataset as a Pandas Dataframe
        * List of quasi-identifiers
        * Sensitive column name
    '''

    df = pd.read_csv(path, header=0, index_col=None, sep=',')
    categorical = ['workclass', 'education', 'marital.status', 'occupation',
        'race', 'sex', 'native.country']
    for name in categorical:
        df[name] = df[name].astype("category")

    return df, ['age', 'workclass', 'education', 'marital.status', 'occupation',
        'race', 'sex', 'native.country'], 'income'
    
def build_data(type='toy', **kwargs):
    '''
    Build data

    Parameters:
        - type: toy, random or adult
        - kwargs: arguments for the underlying data generation functions
    
    Returns:
    - A tuple containing:
        * Dataset as a Pandas Dataframe
        * List of quasi-identifiers
        * Sensitive column name
    '''

    if type == 'toy':
        return build_toy_dataset()
    elif type == 'random':
        return generate_random_dataset(**kwargs)
    elif type == 'adult':
        return read_adult(**kwargs)
    
    return None

def get_k(CHANGE_ME):
    '''
    Obtains the number of different rows within a partition.

    Parameters:
        ...

    Returns:
        - K parameter for k-anonymity
    '''
    ...

def get_l(CHANGE_ME):
    '''
    Gets the number of different sensitive values within a partition.

    Parameters:
        ...

    Returns:
        - L parameter for l-diversity
    '''
    ...

def get_t(CHANGE_ME):
    '''
    Gets the distance between the distribution of the sensitive column within
    the partition with respect to the global distribution.

    Parameters:
        ...
    
    Returns:
        - T parameter for t-closeness
    '''
    ...
def is_k_anonymous(CHANGE_ME, k: int):
    '''
    Checks if a partition is k-anonymous.

    Parameters:
        ...
        - k: number of different rows per partition

    Returns:
        - True if the partition satisfies k-anonymity. False otherwise
    '''
    ...

def is_l_diverse(CHANGE_ME, l: int):
    '''
    Checks if a partition is l-diverse.

    Parameters:
        ...
        - l: number of distinct values for the sensitive column within the partition

    Returns:
        - True if the partition satisfies l-diversity. False otherwise
    '''
    ...

def is_t_close(CHANGE_ME, t: float):
    '''
    Checks if a partition is t-close.

    Parameters:
        ...
        - t: distance between the distribution of the sensitive column within the partition and the global (true) distribution

    Returns:
        - True if the partition satisfies t-closeness. False otherwise
    '''
    ...

def is_valid(CHANGE_ME, k: int, l: Union[None, int] = None, t: Union[None, float] = None):
    '''
    Checks if a partition is valid according to the required anonymity.

    Parameters:
        ...
        - k: number of different rows per partition
        - l: number of distinct values for the sensitive column within the partition
        - t: distance between the distribution of the sensitive column within the partition and the global (true) distribution

    Returns:
        - True if the partition satisfies t-closeness. False otherwise
    '''
    ...
def analyze_dimensions(CHANGE_ME) -> Dict[str, float]:
    '''
    Analyzes the width of each quasi-identifier column within the partition to decide
    on which one to perform the partitioning.

    !TIP: You need to compute relative widhts with respect to the entire database;
    otherwise the numerical columns will be always the chosen ones!

    rel_width = partition_width / global_width
    
    The column with the widest relative range is finally chosen.

    Parameters:
        ...

    Returns:
        - A dictionary containing the width for each quasi-identifier column.
    '''

    widths = {}
    
    # TODO: Compute widths
    ...

    # Sorts columns by width
    return dict(sorted(widths.items(), key=lambda x: -x[1]))

def split(CHANGE_ME) -> Tuple:
    '''
    Splits the partition on the specified quasi-identifier column.

    The split is performed on the median value (for categorical the middle point is computed)

    Parameters:
        ...

    Returns:
        - A tuple containing the two halves of the partition
    '''
    
    ...
    
def build_partitions(database: pd.DataFrame, quasi_identifiers: List[str], sensitive_column: str,
                     k: int, l: Union[int, None]=None, t: Union[float, None]=None) -> List[List[int]]:
    '''
    Builds partitions on the given dataset, so that each one satisfies the specified anonymity.

    Parameters:
        - database: entire database from which the partition is extracted
        - quasi_identifiers: names of the quasi-identifier columns
        - sensitive_column: name of the sensitive column
        - k: number of different rows per partition
        - l: number of distinct values for the sensitive column within the partition
        - t: distance between the distribution of the sensitive column within the partition and the global (true) distribution

    Returns:
        - List of partitions (each partition is a list of indices from the original database)
    '''

    # Partitions that cannot be splitted any more (final partitions)
    partitions = []
    # TODO: Queue those partitions to be processed. Initially, the entire database is the unique available partition!
    queue = [...]

    while queue:
        partition = queue.pop(0)
        widths = analyze_dimensions(...)
        
        # Ensure that widths are sorted!
        for qi in widths:
            lp, rp = split(...)
            # Check if both partitions are valid. If they are not valid, we will try to
            # split them using the next quasi-identifier (sorted by width)
            if is_valid(...) and is_valid(...):
                # We will try to continue to divide each split in the upcoming iterations
                queue.extend((lp, rp))
                break
        else:
            # This else is only executed if the for loop is finished without performing a break!
            # We will only end up here if no valid split is found on any column --> final partition
            # TODO: Be careful here if you work with indices instead of database slices!! You may need to update this append!
            partitions.append(partition)
        
    return partitions
def generalize_numerical(column: pd.Series) -> str:
    '''
    Generalizes a numerical column by computing the min-max range.

    Parameters:
        - column: column values to be generalized

    Returns:
        - Generalized value for the entire sample
    '''

    ...
    
def generalize_categorical(column: pd.Series) -> str:
    '''
    Generalizes a categorical column by grouping all the possible values.

    Parameters:
        - column: column values to be generalized

    Returns:
        - Generalized value for the entire sample
    '''
    
    ...

def generalize(partitions: List[pd.DataFrame], 
               quasi_identifiers: List[str], 
               sensitive_column: str) -> pd.DataFrame:
    '''
    Generalizes each one of the partitions defined for the database.

    Parameters:
        - partitions: list of partitions
        - quasi_identifiers: names of the quasi-identifier columns
        - sensitive_column: name of the sensitive column

    Returns:
        - A DataFrame with generalized values for each partition
    '''

    result = pd.DataFrame()

    result = []

    for num_partition, partition in enumerate(partitions):

        for ix in partition.index:
    
            row = dict()

            # Fill quasi-identifier values
            ...

            # The value of the sensitive column, the original index,
            # and the partition number must be kept for traceability
            row[sensitive_column] = partition.loc[ix, sensitive_column]
            row['index'] = ix
            row['partition'] = num_partition
            result.append(row)
    
    df = pd.DataFrame(result)
    df.set_index('index', inplace=True, drop=True)
    df.index.name = None
    return df

def anonymize(database: pd.DataFrame, quasi_identifiers: List[str], sensitive_column: str,
              k: int, l: Union[int, None]=None, t: Union[float, None]=None) -> pd.DataFrame:
    '''
    Anonymizes a database acording to the required paramters.

    Parameters:
        - database: entire database from which the partition is extracted
        - quasi_identifiers: names of the quasi-identifier columns
        - sensitive_column: name of the sensitive column
        - k: number of different rows per partition
        - l: number of distinct values for the sensitive column within the partition
        - t: distance between the distribution of the sensitive column within the partition and the global (true) distribution

    Returns:
        - List of partitions
    '''
    partitions = build_partitions(database, quasi_identifiers, sensitive_column, k, l=l, t=t)
    return generalize(partitions, quasi_identifiers, sensitive_column)




if __name__ == "__main__":
   # df, quasi_identifiers, sensitive_column = build_data(type='adult', n=5000, path='C:/Users/nuria/Desktop/master/PAN/PAN/p4/anonymity_data/adult.csv')
  #  anonymize(df, quasi_identifiers, sensitive_column, k=2)
   # anonymize(df, quasi_identifiers, sensitive_column, k=2, l=2)
    #anonymize(df, quasi_identifiers, sensitive_column, k=2, l=2, t=0.2)
    import os

# Imprimir la ruta absoluta a la carpeta 'anonymity_data'
print("Ruta absoluta del archivo:", os.path.abspath('anonymity_data/adult.csv'))

# Verifica si el archivo realmente existe en la ruta
print("¿El archivo existe?", os.path.exists('C:/Users/nuria/Desktop/master/PAN/PAN/p4/anonymity_data/adult.csv'))