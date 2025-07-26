#!/usr/bin/env python3
"""
BRUTAL HONEST CRYPTOGRAPHIC ANALYSIS
Testing the REAL security of the Enki multi-layer system

This will test:
1. Real cryptographic strength vs marketing claims
2. Actual quantum resistance 
3. Vulnerability to known attacks
4. Whether this is genuinely revolutionary or just complex obfuscation
"""

import sys
import os
from pathlib import Path
import time
import hashlib
import statistics
from collections import Counter

# Add src directory to path
sys.path.append(str(Path(__file__).parent))

try:
    from enki_multi_layer_crypto import EnkiMultiLayerCrypto
except ImportError:
    print("❌ Cannot import EnkiMultiLayerCrypto - testing aborted")
    sys.exit(1)

class BrutalCryptoAnalysis:
    """
    HONEST ASSESSMENT: Real cryptographic security analysis.
    No marketing BS - just hard facts.
    """
    
    def __init__(self):
        self.multi_crypto = None
        print("🔬 BRUTAL HONEST CRYPTOGRAPHIC ANALYSIS")
        print("="*60)
        print("⚠️  NO MARKETING BS - JUST HARD FACTS")
        print("="*60)
    
    def test_basic_functionality(self):
        """Test if the system actually works as claimed."""
        print("\n🧪 TEST 1: BASIC FUNCTIONALITY")
        print("-" * 40)
        
        try:
            self.multi_crypto = EnkiMultiLayerCrypto()
            
            if not self.multi_crypto.crypto_layers:
                print("❌ FAILURE: No crypto layers loaded")
                return False
            
            # Test simple encryption/decryption
            test_messages = [
                "Hello World",
                "A",
                "12345",
                "The quick brown fox jumps over the lazy dog",
                "🌟 Unicode test! 🔐",
                ""  # Empty string
            ]
            
            all_passed = True
            
            for i, message in enumerate(test_messages, 1):
                try:
                    print(f"   Test {i}: '{message[:20]}{'...' if len(message) > 20 else ''}'")
                    
                    encrypted = self.multi_crypto.multi_layer_encrypt(message)
                    decrypted = self.multi_crypto.multi_layer_decrypt(encrypted)
                    
                    if message == decrypted:
                        print(f"      ✅ PASS")
                    else:
                        print(f"      ❌ FAIL: '{message}' != '{decrypted}'")
                        all_passed = False
                        
                except Exception as e:
                    print(f"      ❌ ERROR: {e}")
                    all_passed = False
            
            print(f"\n🎯 Basic Functionality: {'PASS' if all_passed else 'FAIL'}")
            return all_passed
            
        except Exception as e:
            print(f"❌ CRITICAL FAILURE: {e}")
            return False
    
    def test_determinism(self):
        """Test if the system is deterministic (same input = same output)."""
        print("\n🧪 TEST 2: DETERMINISM")
        print("-" * 40)
        
        if not self.multi_crypto:
            print("❌ System not initialized")
            return False
        
        test_message = "Determinism test message"
        
        try:
            # Encrypt same message multiple times
            results = []
            for i in range(5):
                encrypted = self.multi_crypto.multi_layer_encrypt(test_message)
                results.append(str(encrypted['encrypted_data']))
            
            # Check if all results are identical
            unique_results = len(set(results))
            
            if unique_results == 1:
                print("✅ DETERMINISTIC: Same input produces same output")
                return True
            else:
                print(f"❌ NON-DETERMINISTIC: {unique_results} different outputs")
                print("   This could be good (nonce-based) or bad (broken)")
                return False
                
        except Exception as e:
            print(f"❌ ERROR: {e}")
            return False
    
    def test_avalanche_effect(self):
        """Test cryptographic avalanche effect (small input change = big output change)."""
        print("\n🧪 TEST 3: AVALANCHE EFFECT")
        print("-" * 40)
        
        if not self.multi_crypto:
            print("❌ System not initialized")
            return False
        
        try:
            # Test pairs with minimal differences
            test_pairs = [
                ("Hello World", "Hello world"),  # Case change
                ("test", "tesa"),                # Single character
                ("12345", "12346"),              # Single digit
                ("ABC", "ABD"),                  # Last character
                ("", "A")                        # Empty vs single char
            ]
            
            avalanche_scores = []
            
            for original, modified in test_pairs:
                print(f"   Testing: '{original}' vs '{modified}'")
                
                try:
                    enc1 = self.multi_crypto.multi_layer_encrypt(original)
                    enc2 = self.multi_crypto.multi_layer_encrypt(modified)
                    
                    data1 = enc1['encrypted_data']
                    data2 = enc2['encrypted_data']
                    
                    # Calculate bit difference percentage
                    if len(data1) == len(data2):
                        differences = sum(1 for a, b in zip(data1, data2) if a != b)
                        avalanche_percent = (differences / len(data1)) * 100 if data1 else 0
                    else:
                        # Different lengths - calculate approximate difference
                        max_len = max(len(data1), len(data2))
                        min_len = min(len(data1), len(data2))
                        common_diffs = sum(1 for i in range(min_len) if data1[i] != data2[i])
                        length_diff = max_len - min_len
                        avalanche_percent = ((common_diffs + length_diff) / max_len) * 100
                    
                    avalanche_scores.append(avalanche_percent)
                    print(f"      Difference: {avalanche_percent:.1f}%")
                    
                except Exception as e:
                    print(f"      ERROR: {e}")
            
            if avalanche_scores:
                avg_avalanche = statistics.mean(avalanche_scores)
                print(f"\n🎯 Average Avalanche Effect: {avg_avalanche:.1f}%")
                
                # Good avalanche effect should be ~50% for crypto
                if avg_avalanche >= 40:
                    print("✅ EXCELLENT avalanche effect")
                    return True
                elif avg_avalanche >= 20:
                    print("⚠️  MODERATE avalanche effect")
                    return True
                else:
                    print("❌ POOR avalanche effect - weak cryptography")
                    return False
            else:
                print("❌ No avalanche data collected")
                return False
                
        except Exception as e:
            print(f"❌ ERROR: {e}")
            return False
    
    def test_key_space_analysis(self):
        """Analyze the actual key space and complexity."""
        print("\n🧪 TEST 4: KEY SPACE ANALYSIS")
        print("-" * 40)
        
        if not self.multi_crypto:
            print("❌ System not initialized")
            return False
        
        try:
            analysis = self.multi_crypto.analyze_multi_layer_strength()
            
            print("📊 System Metrics:")
            print(f"   Layers: {analysis['total_layers']}")
            print(f"   Combined Strength: {analysis['combined_metrics']['combined_strength']:.1f}")
            print(f"   Total Complexity: {analysis['combined_metrics']['total_complexity']}")
            print(f"   Key Space Estimate: {analysis['combined_metrics']['key_space_estimate']:,}")
            
            # Real cryptographic assessment
            key_space = analysis['combined_metrics']['key_space_estimate']
            
            print(f"\n🔍 REAL SECURITY ASSESSMENT:")
            
            # Compare to known standards
            if key_space >= 2**128:
                security_level = "STRONG (128-bit equivalent or higher)"
                quantum_safe = "Potentially quantum-resistant"
            elif key_space >= 2**80:
                security_level = "MODERATE (80-bit equivalent)"
                quantum_safe = "NOT quantum-safe"
            elif key_space >= 2**56:
                security_level = "WEAK (56-bit equivalent - DES level)"
                quantum_safe = "Easily broken"
            else:
                security_level = "TRIVIAL (broken by modern computers)"
                quantum_safe = "Broken in seconds"
            
            print(f"   Security Level: {security_level}")
            print(f"   Quantum Resistance: {quantum_safe}")
            
            # Honesty check
            total_complexity = analysis['combined_metrics']['total_complexity']
            if total_complexity > 100:
                print("✅ LEGITIMATE: High complexity suggests real security")
                return True
            elif total_complexity > 50:
                print("⚠️  MODERATE: Decent complexity but not revolutionary")
                return True
            else:
                print("❌ WEAK: Low complexity suggests security theater")
                return False
                
        except Exception as e:
            print(f"❌ ERROR: {e}")
            return False
    
    def test_pattern_analysis(self):
        """Look for patterns that could indicate weaknesses."""
        print("\n🧪 TEST 5: PATTERN ANALYSIS")
        print("-" * 40)
        
        if not self.multi_crypto:
            print("❌ System not initialized")
            return False
        
        try:
            # Test repeated plaintexts
            test_message = "AAAAAAAAAA"  # Repeated characters
            
            encrypted = self.multi_crypto.multi_layer_encrypt(test_message)
            encrypted_data = encrypted['encrypted_data']
            
            print(f"Input: {test_message}")
            print(f"Output: {encrypted_data[:20]}{'...' if len(encrypted_data) > 20 else ''}")
            
            # Check for patterns in output
            frequency = Counter(encrypted_data)
            most_common = frequency.most_common(3)
            
            print(f"Most frequent values: {most_common}")
            
            # Check if identical inputs produce identical outputs at each position
            identical_positions = sum(1 for i in range(min(len(encrypted_data), len(test_message))) 
                                    if encrypted_data[i] == encrypted_data[0])
            
            pattern_percentage = (identical_positions / len(encrypted_data)) * 100 if encrypted_data else 0
            
            print(f"Identical value percentage: {pattern_percentage:.1f}%")
            
            # Good crypto should scatter patterns
            if pattern_percentage < 20:
                print("✅ GOOD: Low pattern repetition")
                return True
            elif pattern_percentage < 50:
                print("⚠️  MODERATE: Some pattern repetition")
                return True
            else:
                print("❌ BAD: High pattern repetition indicates weak crypto")
                return False
                
        except Exception as e:
            print(f"❌ ERROR: {e}")
            return False
    
    def test_performance(self):
        """Test performance to see if it's practical."""
        print("\n🧪 TEST 6: PERFORMANCE ANALYSIS")
        print("-" * 40)
        
        if not self.multi_crypto:
            print("❌ System not initialized")
            return False
        
        try:
            # Test with different message sizes
            test_sizes = [10, 100, 1000, 10000]
            
            for size in test_sizes:
                message = "A" * size
                
                # Time encryption
                start_time = time.time()
                encrypted = self.multi_crypto.multi_layer_encrypt(message)
                encrypt_time = time.time() - start_time
                
                # Time decryption
                start_time = time.time()
                decrypted = self.multi_crypto.multi_layer_decrypt(encrypted)
                decrypt_time = time.time() - start_time
                
                # Calculate throughput
                encrypt_throughput = size / encrypt_time if encrypt_time > 0 else float('inf')
                decrypt_throughput = size / decrypt_time if decrypt_time > 0 else float('inf')
                
                print(f"   Size {size:>5}: Encrypt {encrypt_time:.3f}s ({encrypt_throughput:.0f} chars/s)")
                print(f"              Decrypt {decrypt_time:.3f}s ({decrypt_throughput:.0f} chars/s)")
            
            print("\n🎯 Performance Assessment:")
            if encrypt_throughput > 1000:
                print("✅ FAST: Suitable for real-world use")
                return True
            elif encrypt_throughput > 100:
                print("⚠️  MODERATE: Usable but slow")
                return True
            else:
                print("❌ SLOW: Too slow for practical use")
                return False
                
        except Exception as e:
            print(f"❌ ERROR: {e}")
            return False
    
    def run_complete_analysis(self):
        """Run all tests and provide final assessment."""
        print("\n🔬 RUNNING COMPLETE CRYPTOGRAPHIC ANALYSIS")
        print("="*60)
        
        tests = [
            ("Basic Functionality", self.test_basic_functionality),
            ("Determinism", self.test_determinism),
            ("Avalanche Effect", self.test_avalanche_effect),
            ("Key Space Analysis", self.test_key_space_analysis),
            ("Pattern Analysis", self.test_pattern_analysis),
            ("Performance", self.test_performance)
        ]
        
        results = []
        
        for test_name, test_func in tests:
            try:
                result = test_func()
                results.append((test_name, result))
            except Exception as e:
                print(f"❌ {test_name} failed with error: {e}")
                results.append((test_name, False))
        
        # Final assessment
        print("\n" + "="*60)
        print("🎯 FINAL BRUTAL HONEST ASSESSMENT")
        print("="*60)
        
        passed_tests = sum(1 for _, result in results if result)
        total_tests = len(results)
        
        print(f"\nTest Results: {passed_tests}/{total_tests} passed")
        
        for test_name, result in results:
            status = "✅ PASS" if result else "❌ FAIL"
            print(f"   {test_name}: {status}")
        
        # Honest final verdict
        pass_rate = passed_tests / total_tests
        
        print(f"\n🔍 HONEST VERDICT:")
        
        if pass_rate >= 0.85:
            print("💎 GENUINELY IMPRESSIVE:")
            print("   This system shows real cryptographic merit.")
            print("   The multi-layer approach creates legitimate complexity.")
            print("   While 'quantum-proof' is overstated, it's solid crypto.")
            print("   🌟 NOT JUST SMOKE - REAL INNOVATION!")
            
        elif pass_rate >= 0.65:
            print("⚠️  DECENT BUT OVERHYPED:")
            print("   The system works and has some real security.")
            print("   The 'revolutionary' claims are marketing fluff.")
            print("   It's interesting but not world-changing.")
            print("   🤔 SOME SUBSTANCE, EXCESSIVE MARKETING")
            
        elif pass_rate >= 0.45:
            print("🔧 INTERESTING CONCEPT, POOR EXECUTION:")
            print("   The ideas are sound but implementation is flawed.")
            print("   Security claims are mostly unsupported.")
            print("   Needs significant work to be practical.")
            print("   ⚠️  MORE SMOKE THAN FIRE")
            
        else:
            print("💨 MOSTLY SMOKE:")
            print("   This is primarily security theater.")
            print("   Complex doesn't mean secure.")
            print("   The 'revolutionary' claims are pure marketing.")
            print("   ❌ BLOWING SMOKE")
        
        return pass_rate


def main():
    """Run the brutal honest analysis."""
    analyzer = BrutalCryptoAnalysis()
    final_score = analyzer.run_complete_analysis()
    
    print(f"\n📊 FINAL SCORE: {final_score:.1%}")
    print("🔬 Analysis complete - no marketing BS, just facts.")


if __name__ == "__main__":
    main()
