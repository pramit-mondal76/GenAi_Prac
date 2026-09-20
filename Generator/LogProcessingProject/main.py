def read_file(fileName):
    with open(fileName, "r") as file:
        for line in file :
            yield line.strip()

def filter_lines(logs):
     for log in logs:
         if "ERROR" in log:
             yield log


def extract_error_data(errors):
    for error in errors:

        parts = error.split()

        date = parts[0]
        time = parts[1]
        message = " ".join(parts[3:-1])
        user_id = parts[-1].split("=")[1]

        yield {
            "date": date,
            "time": time,
            "message": message,
            "user_id": int(user_id)
        }

# fileName="logs.txt"
# logs= read_file(fileName)

# error_log = filter_lines(logs)

# for log in error_log:
#     print(log)

# error_data = extract_error_data(error_log)

# for error in error_data:
#     print(error)

def process_logs(fileName):
    logs= read_file(fileName)
    error_log = filter_lines(logs)
    yield from extract_error_data(error_log)

def batch_data(data, batch_size):
    batch=[]
    for item in data:
        batch.append(item)
        if len(batch) == batch_size:
            yield batch
            batch = []
    if batch:
        yield batch


def main():
    processLog= process_logs("logs.txt")
    batched_data = batch_data(processLog, 2)

    for batch in batched_data:
        print ("\n Processing batch :")
        for error in batch:
            print(error)

if __name__ == "__main__":
    main()            