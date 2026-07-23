import dns.resolver
import dns.reversename
import dns.exception # Added to catch timeouts
from ipwhois import IPWhois

def analyze_ip(ip_address):
    print(f"\n🔍 Analyzing IP: {ip_address}")
    
    # --- PHASE 1: Attempt Reverse DNS (PTR Record) ---
    try:
        rev_name = dns.reversename.from_address(ip_address)
        
        # Set a short timeout (e.g., 2 seconds) so your script doesn't freeze up
        answers = dns.resolver.resolve(rev_name, 'PTR', lifetime=2.0)
        
        for rdata in answers:
            return f"Type: Reverse DNS | Owner/Domain: {rdata.to_text()}"
            
    except dns.exception.DNSException as e:
        # This catches NXDOMAIN, NoAnswer, AND LifetimeTimeout
        print(f"ℹ️ Reverse DNS failed or timed out ({type(e).__name__}). Moving to RDAP...")
        
    # --- PHASE 2: Fallback to RDAP / WHOIS Data ---
    try:
        print("📡 Querying official RDAP network registry...")
        obj = IPWhois(ip_address)
        results = obj.lookup_rdap()
        
        network_owner = results.get('asn_description', 'Unknown Organization')
        country = results.get('asn_country_code', 'Unknown')
        
        return f"Type: RDAP Network Block | Owner: {network_owner} [{country}]"
        
    except Exception as e:
        return f"❌ Analysis Failed: {str(e)}"

# --- Test the Fixed Script ---

# This will fall back to RDAP seamlessly even if the DNS times out
print(analyze_ip("167.82.58.172"))
#print(analyze_ip("199.165.136.100"))
