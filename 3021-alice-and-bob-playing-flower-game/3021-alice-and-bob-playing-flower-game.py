class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        m_odd = math.floor(m/2)
        m_even = math.ceil(m/2)
        n_odd = math.floor(n/2)
        n_even = math.ceil(n/2)
        return m_odd * n_even + n_odd*m_even
            
            
        