n, m = map(int, input().split())
n_list = [input() for _ in range(n)]
m_list = [input() for _ in range(m)]


def find_job_bobs(jobs, bobs):
    job_set = set(jobs)
    bob_set = set(bobs)

    job_bobs = list(job_set.intersection(bob_set))

    print(len(job_bobs))

    for job_bob in sorted(job_bobs):
        print(job_bob)


find_job_bobs(n_list, m_list)
